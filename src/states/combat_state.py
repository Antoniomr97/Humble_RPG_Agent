import pygame
from src.core.state import State

class CombatState(State):
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.background_color = (139, 0, 0) # Dark Red for combat

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.map_state import MapState
                # We return to map, but ideally we'd pass the same player data
                self.game.set_state(MapState(self.game, self.player))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(self.background_color)
        
        # Render player
        if "image" in self.player:
            img = pygame.transform.scale(self.player["image"], (100, 100))
            rect = img.get_rect(center=(screen.get_width() // 4, screen.get_height() // 2))
            screen.blit(img, rect)
        
        # Render basic UI
        font = pygame.font.Font(None, 48)
        txt = font.render("COMBATE PROTOTIPO", True, (255, 255, 255))
        screen.blit(txt, (screen.get_width()//2 - txt.get_width()//2, 50))
        
        font_small = pygame.font.Font(None, 24)
        esc_txt = font_small.render("Presiona ESC para volver al mapa", True, (200, 200, 200))
        screen.blit(esc_txt, (screen.get_width()//2 - esc_txt.get_width()//2, screen.get_height() - 50))
