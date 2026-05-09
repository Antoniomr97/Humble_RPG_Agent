import pygame
import math
from src.core.state import State

class MapState(State):
    def __init__(self, game, hero, level=1):
        super().__init__(game)
        self.hero = hero # Ahora es un objeto de clase Hero
        self.level = level
        
        # El camino se alarga según el nivel
        self.path_start_x = 50
        self.path_end_x = 50 + (140 * self.level)
        self.y_line = 300
        
        # Posición inicial del personaje
        self.player_pos = [self.path_start_x, self.y_line]
        self.speed = 250
        self.font = pygame.font.Font(None, 24)
        
        # El encuentro siempre al final del camino actual
        self.encounter_pos = [self.path_end_x, self.y_line]
        self.encounter_radius = 40

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.character_selection import CharacterSelectionState
                self.game.set_state(CharacterSelectionState(self.game))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Movimiento horizontal
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.speed * dt
            
        # Límites del camino
        if self.player_pos[0] < self.path_start_x: self.player_pos[0] = self.path_start_x
        if self.player_pos[0] > self.path_end_x: self.player_pos[0] = self.path_end_x

        # Detección de colisión con el círculo
        dist = math.sqrt((self.player_pos[0] - self.encounter_pos[0])**2 + (self.player_pos[1] - self.encounter_pos[1])**2)
        if dist < self.encounter_radius:
            from src.states.combat_state import CombatState
            self.game.set_state(CombatState(self.game, self.hero, self.level))

    def render(self, screen):
        screen.fill((34, 139, 34)) 
        
        # Dibujar el sendero (línea horizontal)
        pygame.draw.line(screen, (100, 100, 100), (0, self.y_line), (800, self.y_line), 20)
        
        # Punto de encuentro
        pygame.draw.circle(screen, (0, 0, 255), self.encounter_pos, self.encounter_radius, 3)
        label = self.font.render(f"NIVEL {self.level}", True, (255, 255, 255))
        screen.blit(label, (self.encounter_pos[0] - label.get_width()//2, self.encounter_pos[1] - 60))
        
        # Personaje (Objeto Hero)
        if self.hero.image:
            img = pygame.transform.scale(self.hero.image, (100, 100))
            rect = img.get_rect(midbottom=(self.player_pos[0], self.y_line + 10))
            screen.blit(img, rect)
        
        # UI
        txt = self.font.render(f"Progreso: {self.level}/5 | {self.hero.name} | HP: {self.hero.hp}", True, (255, 255, 255))
        screen.blit(txt, (10, 10))
