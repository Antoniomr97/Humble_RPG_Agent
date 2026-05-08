def build_context(agent):
    context = ""

    with open("../docs/architecture.md") as f:
        context += f"\n[ARCHITECTURE]\n{f.read()}\n"

    with open("../docs/game_design.md") as f:
        context += f"\n[GAME DESIGN]\n{f.read()}\n"

    with open("../docs/combat_system.md") as f:
        context += f"\n[COMBAT SYSTEM]\n{f.read()}\n"

    return context