import os
import requests
import json

class OllamaClient:
    def __init__(self, model="qwen2.5-coder:7b", base_url=None):
        self.model = model
        # Use OLLAMA_HOST env var if available, otherwise default to localhost
        env_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self.base_url = base_url or env_host
        
        # Ensure base_url has http/https
        if not self.base_url.startswith("http"):
            # If it's just host:port, add http
            self.base_url = f"http://{self.base_url}"

    def generate(self, prompt):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            return response.json().get("response", "")
        except Exception as e:
            return f"❌ Error calling Ollama API: {e}"

def call_ollama(prompt, model="qwen2.5-coder:7b"):
    client = OllamaClient(model=model)
    return client.generate(prompt)