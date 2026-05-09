import pygame
from src.core.state import State

class MapState(State):
    def __init__(self, game, player_data):
        self.game = game
        self.player = player_data
        self.player_pos = [400, 300]
        self.font = pygame.font.Font(None, 24)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.character_selection import CharacterSelectionState
                self.game.set_state(CharacterSelectionState(self.game))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        speed = 200
        if keys[pygame.K_w]: self.player_pos[1] -= speed * dt
        if keys[pygame.K_s]: self.player_pos[1] += speed * dt
        if keys[pygame.K_a]: self.player_pos[0] -= speed * dt
        if keys[pygame.K_d]: self.player_pos[0] += speed * dt

    def render(self, screen):
        screen.fill((34, 139, 34)) # Verde Bosque
        # Render del personaje seleccionado
        if "image" in self.player:
            img = pygame.transform.scale(self.player["image"], (50, 50))
            screen.blit(img, (self.player_pos[0], self.player_pos[1]))
        
        txt = self.font.render(f"Jugando como: {self.player['name']} (ESC para volver)", True, (255, 255, 255))
        screen.blit(txt, (10, 10))
