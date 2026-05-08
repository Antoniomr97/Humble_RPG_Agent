import pygame
from pygame.locals import *
from src.states.base_state import State
from src.states.battle import CombatState

class MapState(State):
    def __init__(self, manager, player_stats=None):
        super().__init__(manager)
        self.player_stats = player_stats or {'Vida': 50, 'Ataque': 15}
        self.player_pos = [400, 300]
        self.player_speed = 200
        
        self.encounter_pos = [600, 300]
        self.encounter_radius = 40

    def handle_events(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            from src.states.character_selection import CharacterSelectionState
            self.manager.change_state(CharacterSelectionState(self.manager))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.player_pos[1] -= self.player_speed * dt
        if keys[K_DOWN] or keys[K_s]:
            self.player_pos[1] += self.player_speed * dt
        if keys[K_LEFT] or keys[K_a]:
            self.player_pos[0] -= self.player_speed * dt
        if keys[K_RIGHT] or keys[K_d]:
            self.player_pos[0] += self.player_speed * dt

        # Collision with encounter circle
        dist = ((self.player_pos[0] - self.encounter_pos[0])**2 + (self.player_pos[1] - self.encounter_pos[1])**2)**0.5
        if dist < self.encounter_radius:
            print("Encounter triggered!")
            self.manager.push_state(CombatState(self.manager, self.player_stats))

    def render(self, screen):
        screen.fill((34, 139, 34)) # Forest Green
        
        # Draw path line
        pygame.draw.line(screen, (100, 100, 100), (100, 300), (700, 300), 5)
        
        # Draw encounter circle
        pygame.draw.circle(screen, (0, 0, 255), self.encounter_pos, self.encounter_radius, 3)
        font = pygame.font.Font(None, 24)
        label = font.render("COMBAT", True, (0, 0, 255))
        screen.blit(label, (self.encounter_pos[0] - 35, self.encounter_pos[1] - 60))
        
        # Draw player
        pygame.draw.rect(screen, (255, 255, 255), (self.player_pos[0]-15, self.player_pos[1]-15, 30, 30))
