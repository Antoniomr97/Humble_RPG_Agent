import pygame
from src.states.base_state import State

class CharacterSelectionState(State):
    def render(self, screen):
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("Selección de Personaje", True, (0, 0, 0))
        screen.blit(text, (275, 275))

    def update(self, dt):
        pass

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
