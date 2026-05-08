import os

AGENTS_PATH = "../"

def load_agent(name: str):
    base = f"../{name}"

    return {
        "system": open(os.path.join(base, "system.md")).read(),
        "rules": open(os.path.join(base, "rules.md")).read(),
        "prompt": open(os.path.join(base, "prompt.md")).read(),
    }