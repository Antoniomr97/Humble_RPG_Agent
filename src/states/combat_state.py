import pygame
from src.core.state import State

class CombatState(State):
    def __init__(self, game, player, level=1):
        super().__init__(game)
        self.player = player
        self.level = level
        
        # Stats del Enemigo (Rectángulo blanco)
        self.enemy_hp = 20
        self.enemy_atk = 10
        self.enemy_rect = pygame.Rect(550, 250, 100, 100)
        
        # UI & Menú
        self.font_main = pygame.font.Font(None, 48)
        self.font_menu = pygame.font.Font(None, 36)
        self.options = ["ATACAR", "DEFENDER"]
        self.selected_index = 0
        
        self.message = "¡Tu turno!"
        self.combat_active = True
        self.back_button_rect = pygame.Rect(340, 20, 120, 40)

    def handle_events(self, event):
        if not self.combat_active:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                self.check_outcome()
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.process_turn()
            elif event.key == pygame.K_ESCAPE:
                self.return_to_map(self.level)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button_rect.collidepoint(event.pos):
                self.return_to_map(self.level)

    def process_turn(self):
        action = self.options[self.selected_index]
        player_atk = self.player.get('atk', 10)
        
        if action == "ATACAR":
            self.enemy_hp -= player_atk
            self.message = f"¡Atacas! Enemigo pierde {player_atk} HP."
        elif action == "DEFENDER":
            self.message = "¡Te defiendes! El próximo golpe dolerá menos."
            
        # Verificar victoria inmediata
        if self.enemy_hp <= 0:
            self.enemy_hp = 0
            self.message = "¡VICTORIA! Haz clic para avanzar."
            self.combat_active = False
            return

        # Turno del enemigo (Contraataque simple)
        damage = self.enemy_atk
        if action == "DEFENDER":
            damage //= 2
        
        self.player['hp'] -= damage
        self.message += f" | Enemigo ataca: -{damage} HP."

        # Verificar derrota
        if self.player['hp'] <= 0:
            self.player['hp'] = 0
            self.message = "DERROTA... Haz clic para reintentar."
            self.combat_active = False

    def check_outcome(self):
        if self.enemy_hp <= 0:
            # Subir de nivel (máximo 5)
            next_level = min(5, self.level + 1)
            self.return_to_map(next_level)
        else:
            # Reiniciar nivel (recuperar algo de vida para el reintento)
            self.player['hp'] = 50 # Reset HP base
            self.return_to_map(self.level)

    def return_to_map(self, level):
        from src.states.map_state import MapState
        self.game.set_state(MapState(self.game, self.player, level))

    def render(self, screen):
        screen.fill((20, 20, 20))
        
        # Título
        title = self.font_main.render(f"COMBATE - NIVEL {self.level}", True, (200, 0, 0))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 80))

        # Personaje (Izquierda)
        if "image" in self.player:
            img = pygame.transform.scale(self.player["image"], (150, 150))
            screen.blit(img, (150, 220))
            hp_p = self.font_menu.render(f"HP: {self.player['hp']}", True, (0, 255, 0))
            screen.blit(hp_p, (150, 380))

        # Enemigo (Derecha - Rectángulo blanco)
        pygame.draw.rect(screen, (255, 255, 255), self.enemy_rect)
        hp_e = self.font_menu.render(f"ENEMIGO HP: {self.enemy_hp}", True, (255, 255, 255))
        screen.blit(hp_e, (520, 380))

        # Mensaje de combate
        msg_txt = self.font_menu.render(self.message, True, (255, 255, 0))
        screen.blit(msg_txt, (screen.get_width()//2 - msg_txt.get_width()//2, 150))

        # Menú (Si el combate está activo)
        if self.combat_active:
            for i, opt in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (200, 200, 200)
                txt = self.font_menu.render(opt, True, color)
                screen.blit(txt, (screen.get_width()//2 - txt.get_width()//2, 450 + i*40))

        # Botón VOLVER
        pygame.draw.rect(screen, (80, 80, 80), self.back_button_rect, border_radius=5)
        back_txt = self.font_menu.render("VOLVER", True, (255, 255, 255))
        screen.blit(back_txt, (self.back_button_rect.centerx - back_txt.get_width()//2, self.back_button_rect.centery - back_txt.get_height()//2))
