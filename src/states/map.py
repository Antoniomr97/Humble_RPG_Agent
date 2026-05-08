import pygame
from pygame.locals import *
from states.state import State

class MapState(State):
    def __init__(self, game):
        super().__init__(game)
        self.player = {
            'Vida': 50,
            'Ataque': 15
        }
        self.player_pos = [pygame.display.get_surface().get_width() // 2, pygame.display.get_surface().get_height() // 2]
        self.encounter_circle_radius = 30
        self.encounter_circle_pos = [pygame.display.get_surface().get_width() // 4, pygame.display.get_surface().get_height() // 4]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.player_pos[1] -= 5
        if keys[K_DOWN] or keys[K_s]:
            self.player_pos[1] += 5
        if keys[K_LEFT] or keys[K_a]:
            self.player_pos[0] -= 5
        if keys[K_RIGHT] or keys[K_d]:
            self.player_pos[0] += 5

        distance = ((self.player_pos[0] - self.encounter_circle_pos[0]) ** 2 + (self.player_pos[1] - self.encounter_circle_pos[1]) ** 2) ** 0.5
        if distance <= self.encounter_circle_radius:
            self.game.change_state('battle')

    def draw(self, surface):
        surface.fill((0, 255, 0))
        pygame.draw.circle(surface, (255, 0, 0), self.player_pos, 10)
        pygame.draw.circle(surface, (0, 0, 255), self.encounter_circle_pos, self.encounter_circle_radius, 2)
