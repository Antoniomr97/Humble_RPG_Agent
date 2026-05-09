from src.core.engine import Game

class State:
    def __init__(self, game):
        self.game = game

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_events(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass

