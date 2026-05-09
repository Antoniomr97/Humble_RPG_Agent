from src.core.engine import Game
from src.core.state import State

class MapState(State):
    def __init__(self, game: Game):
        super().__init__(game)
        self.character_sprite = pygame.image.load("path/to/character_sprite.png")
        self.character_rect = self.character_sprite.get_rect()
        self.scale_factor = 1.5
        self.character_sprite = pygame.transform.scale(self.character_sprite, (int(self.character_rect.width * self.scale_factor), int(self.character_rect.height * self.scale_factor)))

    def handle_events(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        screen.blit(self.character_sprite, (100, 100))  # Adjust position as needed
