import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # agents/

def load_agent(name: str):
    base = os.path.join(BASE_DIR, name)

    system_path = os.path.join(base, "system.md")

    if not os.path.exists(system_path):
        raise FileNotFoundError(f"Missing system.md for agent: {name}")

    return {
        "system": open(system_path, "r", encoding="utf-8").read()
    }