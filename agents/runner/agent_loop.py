import os
from .ollama_client import OllamaClient
from .context_builder import build_context
from .executor import write_files_from_response


class AgentRunner:
    def __init__(self, model="qwen2.5-coder:7b"):
        self.client = OllamaClient(model=model)

    def run(self, repo_path, goal, agent_prompt, agent_name="Agent"):
        """
        Main agent loop:
        1. Build repo context
        2. Send to model
        3. Parse response
        4. Write files
        """

        # 1. CONTEXT BUILDING
        print(f"🔍 Building context for {os.path.basename(os.path.abspath(repo_path))}...")
        context = build_context(repo_path)

        full_prompt = self._build_prompt(context, goal, agent_prompt, agent_name)

        # 2. CALL MODEL
        print(f"🤖 {agent_name} is thinking (model: {self.client.model})...")
        response = self.client.generate(full_prompt)

        # 3. EXECUTE OUTPUT (WRITE FILES)
        print("⚡ Processing generated code...")
        write_files_from_response(repo_path, response)

        return response

    def _build_prompt(self, context, goal, agent_prompt, agent_name):
        return f"""
You are the {agent_name} of the project.

--- AGENT SYSTEM PROMPT ---
{agent_prompt}

--- PROJECT CONTEXT ---
{context}

--- CURRENT TASK / GOAL ---
{goal}

--- CRITICAL OUTPUT RULES ---
1. You MUST return the output using the following format for EACH file you want to create or modify:

# file: path/to/file.py
```python
# content here
```

2. ABSOLUTE IMPORTS: All imports MUST be absolute and start with `src.` (e.g., `from src.core.engine import Game`). Never use relative imports or omit the `src.` prefix.
3. ARCHITECTURE COMPLIANCE: Respect the architecture in `docs/architecture.md`. Use `handle_events(self, event)`, `update(self, dt)`, and `render(self, screen)` methods for all States.
4. FULL CONTENT: If you are modifying an existing file, you MUST provide the FULL content of the file.
5. NO EXPLANATIONS: Do NOT include any explanations or conversational text outside of the file blocks.
"""