from src.core.engine import Game
from src.states.character_selection import CharacterSelectionState
from src.core.state_manager import StateManager

def main():
    game = Game()
    state_manager = StateManager(CharacterSelectionState())
    game.set_state_manager(state_manager)
    game.run()

if __name__ == "__main__":
    main()
