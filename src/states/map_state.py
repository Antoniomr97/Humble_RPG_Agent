from src.core.state import State
import pygame

class MapState(State):
    def __init__(self, game, player_data):
        super().__init__(game)
        self.player = player_data['player']
        self.level = player_data['level']
        self.max_level = 5
        self.path_length = 150 * self.level
        self.character_y_position = self.game.screen_height // 2

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.player.x >= self.path_length:
                player_data = {
                    'player': self.player,
                    'level': self.level
                }
                self.game.set_state(CombatState(self.game, player_data))

    def update(self, dt):
        # Update logic for MapState
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))  # White background
        pygame.draw.line(screen, (0, 0, 0), (0, self.character_y_position), (self.path_length, self.character_y_position), 10)
        pygame.draw.circle(screen, (0, 0, 255), (self.path_length, self.character_y_position), 20)  # Blue circle at the end of the path
        pygame.draw.rect(screen, (0, 0, 0), (self.player.x, self.character_y_position - 25, 50, 50))  # Character

# file: src/states/combat_state.py
