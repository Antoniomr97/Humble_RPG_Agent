import os
import re


FILE_PATTERN = r"# file:\s*(.+?)\s*\n```(?:python|py)?\n(.*?)```"


def safe_path(repo_path, file_path):
    """
    Evita path traversal tipo ../../
    """
    full_path = os.path.abspath(os.path.join(repo_path, file_path))
    repo_abs = os.path.abspath(repo_path)

    if not full_path.startswith(repo_abs):
        raise ValueError(f"Unsafe path detected: {file_path}")

    return full_path


def write_files_from_response(repo_path, response):
    matches = re.findall(FILE_PATTERN, response, re.DOTALL)

    if not matches:
        print("❌ No files found in response")
        print("DEBUG RESPONSE:\n", response[:1000])
        return

    print(f"📦 Files detected: {len(matches)}")

    for path, code in matches:
        try:
            full_path = safe_path(repo_path, path.strip())

            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            cleaned_code = code.strip() + "\n"

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(cleaned_code)

            print(f"✅ Written: {full_path}")

        except Exception as e:
            print(f"❌ Error writing {path}: {e}")