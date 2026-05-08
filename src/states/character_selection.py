import pygame
from pygame.locals import *
from states.state import State

class CharacterSelectionState(State):
    def __init__(self, game):
        super().__init__(game)
        self.colors = {
            'Pícaro': (255, 69, 0),  # Vermillion
            'Guerrero': (221, 160, 221),  # Backnister
            'Mago': (0, 139, 139)  # Gandall
        }
        self.stats = {
            'Pícaro': {'Vida': 50, 'Ataque': 15},
            'Guerrero': {'Vida': 70, 'Ataque': 20},
            'Mago': {'Vida': 40, 'Ataque': 30}
        }
        self.selected_character = None
        self.character_rects = []

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.game.change_state('menu')
            elif event.type == MOUSEBUTTONDOWN:
                for rect, character in zip(self.character_rects, self.colors.keys()):
                    if rect.collidepoint(event.pos):
                        self.selected_character = character
                        self.game.player = self.stats[character]
                        self.game.change_state('map')

    def draw(self, surface):
        surface.fill((0, 0, 0))
        width, height = surface.get_size()
        for i, (name, color) in enumerate(self.colors.items()):
            x = width // 3 * i
            y = height // 2
            rect = pygame.Rect(x, y, width // 3, height // 3)
            pygame.draw.rect(surface, color, rect)
            font = pygame.font.Font(None, 36)
            text_name = font.render(name, True, (0, 0, 0))
            text_stats = font.render(f"Vida: {self.stats[name]['Vida']}, Ataque: {self.stats[name]['Ataque']}", True, (0, 0, 0))
            surface.blit(text_name, (x + 10, y + 10))
            surface.blit(text_stats, (x + 10, y + 50))
            self.character_rects.append(rect)
