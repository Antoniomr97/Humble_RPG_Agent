import pygame
from pygame.locals import *
from src.states.base_state import State

class CombatState(State):
    def __init__(self, manager, player_stats):
        super().__init__(manager)
        self.player_stats = player_stats
        self.enemy_stats = {'Vida': 50, 'Ataque': 10}

    def handle_events(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # Return to map
            self.manager.pop_state()

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((50, 0, 0)) # Dark Red background
        
        width, height = screen.get_size()
        
        # Draw Player (Left)
        pygame.draw.rect(screen, (0, 255, 0), (150, height//2 - 50, 100, 100))
        
        # Draw Enemy (Right)
        pygame.draw.rect(screen, (255, 0, 0), (width - 250, height//2 - 50, 100, 100))
        
        # UI
        font = pygame.font.Font(None, 48)
        title = font.render("COMBATE INICIADO", True, (255, 255, 255))
        screen.blit(title, (width//2 - title.get_width()//2, 100))
        
        font_small = pygame.font.Font(None, 24)
        info = font_small.render("Presiona ESC para huir (Volver al mapa)", True, (200, 200, 200))
        screen.blit(info, (width//2 - info.get_width()//2, height - 50))
