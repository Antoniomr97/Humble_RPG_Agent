from runner.loader import load_agent
from runner.ollama_client import call_ollama
from runner.context_builder import build_context

def run(agent_name: str, task: str):
    agent = load_agent(agent_name)

    context = build_context(agent)

    prompt = f"""
{agent['system']}

TASK:
{task}

CONTEXT:
{context}
"""

    response = call_ollama(prompt, model="qwen2.5-coder")

    print("\n=== RESPONSE ===\n")
    print(response)


if __name__ == "__main__":
    while True:
        agent = input("Agent (architect/gameplay/reviewer): ")
        task = input("Task: ")

        run(agent, task)