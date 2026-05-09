import pygame
from src.core.state import State

class CombatState(State):
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.background_color = (30, 0, 0) # Darker Red for premium look
        
        self.font_main = pygame.font.Font(None, 48)
        self.font_menu = pygame.font.Font(None, 36)
        
        # Lógica del menú
        self.options = ["ATACAR", "DEFENDER"]
        self.selected_index = 0
        
        # Botón Volver
        self.back_button_rect = pygame.Rect(340, 20, 120, 40)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.execute_action()
            elif event.key == pygame.K_ESCAPE:
                self.return_to_map()
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button_rect.collidepoint(event.pos):
                self.return_to_map()

    def execute_action(self):
        action = self.options[self.selected_index]
        if action == "ATACAR":
            print(f"¡{self.player['name']} ataca con {self.player['atk']} de daño!")
        elif action == "DEFENDER":
            print(f"¡{self.player['name']} se defiende! Daño reducido al 50%")

    def return_to_map(self):
        from src.states.map_state import MapState
        self.game.set_state(MapState(self.game, self.player))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(self.background_color)
        
        # Dibujar degradado simple de fondo
        for i in range(screen.get_height()):
            color = (max(0, 30 - i//20), 0, 0)
            pygame.draw.line(screen, color, (0, i), (screen.get_width(), i))

        # Render del personaje (Grande)
        if "image" in self.player:
            img = pygame.transform.scale(self.player["image"], (200, 200))
            rect = img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(img, rect)
        
        # Menú de combate (debajo del personaje)
        menu_y_start = screen.get_height() // 2 + 100
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_index else (150, 150, 150)
            txt = self.font_menu.render(option, True, color)
            pos_x = screen.get_width() // 2 - txt.get_width() // 2
            pos_y = menu_y_start + (i * 40)
            
            # Subrayado si está seleccionado
            if i == self.selected_index:
                pygame.draw.line(screen, (255, 255, 0), (pos_x, pos_y + txt.get_height()), (pos_x + txt.get_width(), pos_y + txt.get_height()), 2)
                txt = self.font_menu.render(option, True, (255, 255, 0)) # Amarillo para selección
                
            screen.blit(txt, (pos_x, pos_y))

        # Botón VOLVER (Superior)
        pygame.draw.rect(screen, (100, 100, 100), self.back_button_rect, border_radius=5)
        pygame.draw.rect(screen, (200, 200, 200), self.back_button_rect, 2, border_radius=5)
        back_txt = self.font_menu.render("VOLVER", True, (255, 255, 255))
        screen.blit(back_txt, (self.back_button_rect.centerx - back_txt.get_width()//2, self.back_button_rect.centery - back_txt.get_height()//2))

        # Título
        title = self.font_main.render("FASE DE COMBATE", True, (255, 255, 255))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 80))
