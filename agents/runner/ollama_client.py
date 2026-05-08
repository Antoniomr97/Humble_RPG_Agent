import subprocess

def call_ollama(prompt, model="qwen2.5-coder:7b"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout