import os

def apply_changes(response: str):
    """
    Interpreta la salida del agente y aplica cambios al proyecto.
    Versión simple: detecta bloques de creación de archivos.
    """

    lines = response.split("\n")

    current_file = None
    buffer = []

    for line in lines:

        # Detectar inicio de archivo
        if line.startswith("FILE:"):
            current_file = line.replace("FILE:", "").strip()
            buffer = []

        # Detectar fin de archivo
        elif line.startswith("END FILE"):
            if current_file:
                os.makedirs(os.path.dirname(current_file), exist_ok=True)

                with open(current_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(buffer))

                print(f"✔ Archivo creado: {current_file}")

            current_file = None
            buffer = []

        else:
            if current_file:
                buffer.append(line)