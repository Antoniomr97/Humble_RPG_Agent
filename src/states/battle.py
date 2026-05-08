import pygame
from pygame.locals import *
from states.state import State

class BattleState(State):
    def __init__(self, game):
        super().__init__(game)
        self.player = {
            'Vida': 50,
            'Ataque': 15
        }
        self.enemy = {
            'Vida': 40,
            'Ataque': 20
        }

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.game.change_state('map')

    def draw(self, surface):
        surface.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        player_text = font.render(f"Jugador: Vida {self.player['Vida']}, Ataque {self.player['Ataque']}", True, (255, 255, 255))
        enemy_text = font.render(f"Enemigo: Vida {self.enemy['Vida']}, Ataque {self.enemy['Ataque']}", True, (255, 255, 255))
        surface.blit(player_text, (10, 10))
        surface.blit(enemy_text, (10, 50))

        pygame.draw.rect(surface, (0, 255, 0), (pygame.display.get_surface().get_width() // 4, pygame.display.get_surface().get_height() // 2, 100, 100))
        pygame.draw.rect(surface, (255, 0, 0), (3 * pygame.display.get_surface().get_width() // 4, pygame.display.get_surface().get_height() // 2, 100, 100))
