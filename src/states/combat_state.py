import pygame
import random
from src.core.state import State
from src.entities.enemy import Enemy

class CombatState(State):
    def __init__(self, game, hero, level=1):
        super().__init__(game)
        self.hero = hero
        self.level = level
        
        # Instanciamos un enemigo aleatorio usando la nueva clase
        self.enemy = Enemy()
        self.enemy_rect = pygame.Rect(550, 250, 100, 100)
        
        # UI & Menú
        self.font_main = pygame.font.Font(None, 64)
        self.font_menu = pygame.font.Font(None, 36)
        self.options = ["ATACAR", "DEFENDER"]
        self.selected_index = 0
        
        # Estados de Animación
        self.message = f"¡Un {self.enemy.name} salvaje aparece!"
        self.combat_active = True
        self.game_over = False
        self.shake_amount = 0
        self.shake_timer = 0
        self.floating_texts = [] 
        
        self.back_button_rect = pygame.Rect(340, 20, 120, 40)

    def handle_events(self, event):
        if self.game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                from src.states.character_selection import CharacterSelectionState
                self.game.set_state(CharacterSelectionState(self.game))
            return

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
        
        # Ataque del Héroe (Daño aleatorio)
        if action == "ATACAR":
            dmg = self.hero.calculate_attack()
            self.enemy.take_damage(dmg)
            self.add_floating_text(f"-{dmg}", (600, 250))
            self.trigger_shake(10)
            self.message = f"¡Atacas al {self.enemy.name}! -{dmg} HP."
        elif action == "DEFENDER":
            self.message = "¡Te pones en guardia!"
            
        if self.enemy.hp <= 0:
            if self.level >= 5:
                self.game_over = True
            else:
                self.message = f"¡{self.enemy.name} derrotado! Haz clic para avanzar."
            self.combat_active = False
            return

        # Contraataque del Enemigo (Daño aleatorio)
        dmg_enemy = self.enemy.calculate_attack()
        if action == "DEFENDER": dmg_enemy //= 2
        
        self.hero.take_damage(dmg_enemy)
        self.add_floating_text(f"-{dmg_enemy}", (220, 250))
        self.trigger_shake(5)
        self.message += f" | {self.enemy.name} ataca: -{dmg_enemy} HP."

        if self.hero.hp <= 0:
            self.message = "DERROTA... Haz clic para reintentar."
            self.combat_active = False

    def add_floating_text(self, text, pos):
        self.floating_texts.append({"text": text, "x": pos[0], "y": pos[1], "timer": 60, "alpha": 255})

    def trigger_shake(self, amount):
        self.shake_amount = amount
        self.shake_timer = 15

    def check_outcome(self):
        if self.enemy.hp <= 0:
            self.return_to_map(min(5, self.level + 1))
        else:
            self.hero.hp = self.hero.max_hp
            self.return_to_map(self.level)

    def return_to_map(self, level):
        from src.states.map_state import MapState
        self.game.set_state(MapState(self.game, self.hero, level))

    def update(self, dt):
        if self.shake_timer > 0: self.shake_timer -= 1
        else: self.shake_amount = 0
            
        for ft in self.floating_texts[:]:
            ft["y"] -= 1
            ft["timer"] -= 1
            ft["alpha"] -= 4
            if ft["timer"] <= 0: self.floating_texts.remove(ft)

    def render(self, screen):
        screen.fill((15, 15, 20))
        off_x = random.randint(-self.shake_amount, self.shake_amount) if self.shake_timer > 0 else 0
        
        if self.game_over:
            self.render_victory(screen)
            return

        # Héroe
        if self.hero.image:
            img = pygame.transform.scale(self.hero.image, (150, 150))
            pos_x, pos_y = 150 + off_x, 220
            screen.blit(img, (pos_x, pos_y))
            hp_txt = self.font_menu.render(f"HP: {self.hero.hp}", True, (0, 255, 0))
            screen.blit(hp_txt, (pos_x + 75 - hp_txt.get_width()//2, pos_y + 160))

        # Enemigo (Usamos color según el tipo)
        enemy_x, enemy_y = self.enemy_rect.x + off_x, self.enemy_rect.y
        pygame.draw.rect(screen, self.enemy.image, (enemy_x, enemy_y, 100, 100))
        hp_e = self.font_menu.render(f"HP: {self.enemy.hp}", True, (255, 255, 255))
        screen.blit(hp_e, (enemy_x + 50 - hp_e.get_width()//2, enemy_y + 110))
        name_e = self.font_menu.render(self.enemy.name, True, (255, 255, 255))
        screen.blit(name_e, (enemy_x + 50 - name_e.get_width()//2, enemy_y - 30))

        # Efectos y UI
        for ft in self.floating_texts:
            t = self.font_menu.render(ft["text"], True, (255, 0, 0))
            t.set_alpha(ft["alpha"])
            screen.blit(t, (ft["x"], ft["y"]))

        msg = self.font_menu.render(self.message, True, (255, 255, 0))
        screen.blit(msg, (screen.get_width()//2 - msg.get_width()//2, 150))

        if self.combat_active:
            for i, opt in enumerate(self.options):
                color = (255, 255, 0) if i == self.selected_index else (180, 180, 180)
                txt = self.font_menu.render(opt, True, color)
                pos_x = screen.get_width() // 2 - txt.get_width() // 2
                pos_y = 450 + i*40
                if i == self.selected_index:
                    pygame.draw.line(screen, (255, 255, 0), (pos_x, pos_y + 30), (pos_x + txt.get_width(), pos_y + 30), 2)
                screen.blit(txt, (pos_x, pos_y))

        pygame.draw.rect(screen, (60, 60, 80), self.back_button_rect, border_radius=5)
        b_txt = self.font_menu.render("VOLVER", True, (255, 255, 255))
        screen.blit(b_txt, (self.back_button_rect.centerx - b_txt.get_width()//2, self.back_button_rect.centery - b_txt.get_height()//2))

    def render_victory(self, screen):
        txt = self.font_main.render("¡BIEN HECHO!", True, (255, 215, 0))
        screen.blit(txt, (screen.get_width()//2 - txt.get_width()//2, screen.get_height()//2 - 50))
        sub = self.font_menu.render("Has completado la aventura. Haz clic para reiniciar.", True, (200, 200, 200))
        screen.blit(sub, (screen.get_width()//2 - sub.get_width()//2, screen.get_height()//2 + 50))
