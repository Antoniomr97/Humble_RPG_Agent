from agents.runner.loader import load_agent
from agents.runner.ollama_client import call_ollama
from agents.runner.context_builder import build_context
from agents.runner.executor import write_files_from_response


def run(agent_name: str, task: str):
    agent = load_agent(agent_name)

    context = build_context(".")

    prompt = f"""
{agent['system']}

TASK:
{task}

PROJECT CONTEXT:
{context}

RULES:
- Return ONLY structured file output
- NO explanations
"""

    response = call_ollama(prompt)

    print(response)

    write_files_from_response(".", response)


if __name__ == "__main__":
    print("🚀 Agent System Started")

    while True:
        agent = input("Agent (architect/gameplay/reviewer): ")
        task = input("Task: ")

        run(agent, task)