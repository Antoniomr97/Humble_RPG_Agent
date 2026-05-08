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

2. Do NOT include any explanations or conversational text outside of the file blocks.
3. Ensure all imports are correct according to the project structure.
4. If you are modifying an existing file, you MUST provide the FULL content of the file.
5. Return ONLY the files that need to be created or modified.
"""