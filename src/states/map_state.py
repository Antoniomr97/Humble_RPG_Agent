import pygame
import math
from src.core.state import State

class MapState(State):
    def __init__(self, game, player_data):
        self.game = game
        self.player = player_data
        # Posicionamos al personaje en la línea central (Y=300)
        self.player_pos = [100, 300]
        self.speed = 250
        self.font = pygame.font.Font(None, 24)
        
        # Configuración del encuentro
        self.encounter_pos = [600, 300]
        self.encounter_radius = 30

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from src.states.character_selection import CharacterSelectionState
                self.game.set_state(CharacterSelectionState(self.game))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Movimiento solo en el eje X
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.speed * dt
            
        # Límites de la pantalla para el eje X
        if self.player_pos[0] < 50: self.player_pos[0] = 50
        if self.player_pos[0] > 750: self.player_pos[0] = 750

        # Detección de colisión con el círculo de combate
        dist = math.sqrt((self.player_pos[0] - self.encounter_pos[0])**2 + (self.player_pos[1] - self.encounter_pos[1])**2)
        if dist < self.encounter_radius:
            print("¡Combate iniciado!")
            from src.states.combat_state import CombatState
            self.game.set_state(CombatState(self.game, self.player))

    def render(self, screen):
        # Fondo bosque
        screen.fill((34, 139, 34)) 
        
        # Dibujar el camino (línea horizontal)
        pygame.draw.line(screen, (100, 100, 100), (0, 300), (800, 300), 10)
        
        # Dibujar el punto de encuentro
        pygame.draw.circle(screen, (0, 0, 255), self.encounter_pos, self.encounter_radius, 3)
        label = self.font.render("COMBATE", True, (0, 0, 255))
        screen.blit(label, (self.encounter_pos[0] - label.get_width()//2, self.encounter_pos[1] - 50))
        
        # Render del personaje seleccionado
        if "image" in self.player:
            # Escalamos la imagen para que encaje bien en el camino
            img = pygame.transform.scale(self.player["image"], (60, 60))
            # Dibujamos centrado en la posición
            rect = img.get_rect(center=(self.player_pos[0], self.player_pos[1]))
            screen.blit(img, rect)
        
        # UI superior
        txt = self.font.render(f"Jugador: {self.player['name']} | Usa A/D para moverte | ESC para salir", True, (255, 255, 255))
        # Fondo para el texto
        s = pygame.Surface((txt.get_width() + 20, 30))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        screen.blit(txt, (10, 5))
