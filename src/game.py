from src.core.engine import Game
from src.states.character_selection import CharacterSelectionState

def main():
    # Inicializamos el motor
    game = Game()
    
    # Creamos el primer estado y lo asignamos
    initial_state = CharacterSelectionState(game)
    game.set_state(initial_state)
    
    # Arrancamos
    game.run()

if __name__ == "__main__":
    main()
