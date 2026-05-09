from src.core.state import State
from src.entities.hero import Hero

class CharacterSelection(State):
    def __init__(self, game):
        super().__init__(game)
        self.heroes = [
            Hero(hp=100, max_hp=100, atk=20, name="Hero 1", image=None),
            Hero(hp=120, max_hp=120, atk=25, name="Hero 2", image=None),
            Hero(hp=90, max_hp=90, atk=18, name="Hero 3", image=None)
        ]
        self.selected_hero = None

    def handle_events(self, event):
        # Handle events to select a hero
        pass

    def update(self, dt):
        # Update logic
        pass

    def render(self, screen):
        # Render the character selection screen
        pass
