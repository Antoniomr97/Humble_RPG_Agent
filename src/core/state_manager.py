from src.core.engine import Game
from src.core.state import State

class StateManager:
    def __init__(self, game):
        self.game = game
        self.current_state = None

    def set_state(self, state_class):
        self.current_state = state_class(self.game)

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)

    def render(self, screen):
        if self.current_state:
            self.current_state.render(screen)
