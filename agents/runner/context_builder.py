import os

ALLOWED_EXTENSIONS = {'.py', '.md', '.txt', '.json'}
IGNORE_DIRS = {'env', '__pycache__', '.git', '.vscode', 'assets', 'scratch'}

def build_context(repo_path):
    context_parts = []
    
    # 1. First, show the project structure
    structure = ["PROJECT STRUCTURE:"]
    for root, dirs, files in os.walk(repo_path):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        level = root.replace(repo_path, "").count(os.sep)
        indent = "  " * level
        structure.append(f"{indent}{os.path.basename(root)}/")
        
        for f in files:
            structure.append(f"{indent}  {f}")
    
    context_parts.append("\n".join(structure))
    context_parts.append("\n" + "="*40 + "\n")
    context_parts.append("FILE CONTENTS:")

    # 2. Then, include actual content of relevant files
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ALLOWED_EXTENSIONS:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, repo_path)
                
                try:
                    with open(full_path, "r", encoding="utf-8") as file:
                        content = file.read()
                        context_parts.append(f"\n--- FILE: {rel_path} ---\n{content}")
                except Exception as e:
                    context_parts.append(f"\n--- FILE: {rel_path} ---\nError reading file: {e}")

    return "\n".join(context_parts)