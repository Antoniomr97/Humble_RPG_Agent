import os
from ollama_client import OllamaClient
from context_builder import build_context
from executor import write_files_from_response


class AgentRunner:
    def __init__(self, model="qwen2.5-coder:7b"):
        self.client = OllamaClient(model=model)

    def run(self, repo_path, goal, agent_prompt):
        """
        Main agent loop:
        1. Build repo context
        2. Send to model
        3. Parse response
        4. Write files
        5. (optional) iterate
        """

        # 1. CONTEXT BUILDING
        context = build_context(repo_path)

        full_prompt = self._build_prompt(context, goal, agent_prompt)

        # 2. CALL MODEL
        response = self.client.generate(full_prompt)

        # 3. EXECUTE OUTPUT (WRITE FILES)
        write_files_from_response(repo_path, response)

        return response

    def _build_prompt(self, context, goal, agent_prompt):
        return f"""
You are an expert Architect Agent working on a Python Pygame project.

--- PROJECT CONTEXT ---
{context}

--- GOAL ---
{goal}

--- AGENT RULES ---
{agent_prompt}

--- CRITICAL RULES ---
- You MUST output only files
- You MUST ensure code is runnable
- You MUST ensure imports match repo structure
- You MUST NOT hallucinate missing files

Return format:
# file: path
<code>
"""