import os
import re


FILE_PATTERN = r"# file:\s*(.+?)\s*\n```[\w-]*\n(.*?)```"


def safe_path(repo_path, file_path):
    """
    Evita path traversal tipo ../../ y asegura que la ruta esté dentro del repo.
    """
    # Normalizamos la ruta quitando slashes iniciales para evitar que join la trate como absoluta
    clean_file_path = file_path.strip().lstrip('/\\')
    
    repo_abs = os.path.abspath(repo_path)
    full_path = os.path.abspath(os.path.join(repo_abs, clean_file_path))

    if not full_path.startswith(repo_abs):
        raise ValueError(f"Security: Path '{full_path}' is outside of repository '{repo_abs}'")

    return full_path


def write_files_from_response(repo_path, response):
    matches = re.findall(FILE_PATTERN, response, re.DOTALL)

    if not matches:
        print("⚠️ No files found in response")
        # Print a snippet of the response for debugging
        print("-" * 20)
        print("DEBUG RESPONSE (first 300 chars):")
        print(response[:300])
        print("-" * 20)
        return

    print(f"📦 Files detected: {len(matches)}")

    for path, code in matches:
        try:
            full_path = safe_path(repo_path, path.strip())

            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            cleaned_code = code.strip() + "\n"

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(cleaned_code)

            print(f"✅ Written: {os.path.relpath(full_path, repo_path)}")

        except Exception as e:
            print(f"❌ Error writing {path}: {str(e)}")