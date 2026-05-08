import os


def build_context(repo_path):
    structure = []

    for root, dirs, files in os.walk(repo_path):
        # ignorar venv y basura
        if "env" in root or "__pycache__" in root:
            continue

        level = root.replace(repo_path, "").count(os.sep)
        indent = "  " * level

        structure.append(f"{indent}{os.path.basename(root)}/")

        for f in files:
            structure.append(f"{indent}  {f}")

    return "\n".join(structure)