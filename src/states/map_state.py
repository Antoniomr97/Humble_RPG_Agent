from src.core.state_manager import StateManager
from src.core.engine import Game
import pygame

class MapState(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player
        self.background_color = (0, 0, 0)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_state(StateManager.CHARACTER_SELECTION_STATE)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(self.background_color)
        player_image_rect = self.player["image"].get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(self.player["image"], player_image_rect)
        pygame.display.flip()
