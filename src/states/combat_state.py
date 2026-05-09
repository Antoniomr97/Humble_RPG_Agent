import pygame
import math
from src.core.engine import Game
from src.core.state import State

class CombatState(State):
    def __init__(self, game, player_data):
        super().__init__(game)
        self.player = player_data['player']
        self.enemy = player_data['enemy']
        self.font = pygame.font.Font(None, 36)
        self.damage_numbers = []
        self.vibration_start_time = None
        self.vibration_offset = 0
        self.won_combat = False

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.won_combat:
                self.player_attack()

    def player_attack(self):
        damage = self.player.attack()
        self.enemy.take_damage(damage)
        self.damage_numbers.append((self.enemy.rect.centerx, self.enemy.rect.top - 20, damage, pygame.time.get_ticks()))
        self.vibration_start_time = pygame.time.get_ticks()

    def update(self, dt):
        current_time = pygame.time.get_ticks()
        if self.vibration_start_time is not None and current_time - self.vibration_start_time < 200:
            self.vibration_offset = (math.sin((current_time - self.vibration_start_time) / 10.0) * 2)
        else:
            self.vibration_offset = 0
            self.vibration_start_time = None

        if not self.won_combat and self.enemy.is_alive():
            if current_time - self.last_enemy_attack_time > 1000:
                self.enemy_attack()

        for i, (x, y, damage, start_time) in enumerate(self.damage_numbers):
            elapsed_time = current_time - start_time
            if elapsed_time < 1000:
                alpha = max(255 - int(elapsed_time / 10), 0)
                text_surface = self.font.render(str(damage), True, (255, 0, 0))
                text_surface.set_alpha(alpha)
                self.screen.blit(text_surface, (x, y - elapsed_time // 3))
            else:
                del self.damage_numbers[i]

        if not self.enemy.is_alive() and self.player.level == 5:
            self.won_combat = True

    def enemy_attack(self):
        damage = self.enemy.attack()
        self.player.take_damage(damage)
        self.damage_numbers.append((self.player.rect.centerx, self.player.rect.top - 20, damage, pygame.time.get_ticks()))
        self.last_enemy_attack_time = pygame.time.get_ticks()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.render_health_bars(screen)
        if self.won_combat:
            self.render_victory_screen(screen)
        else:
            self.render_characters(screen)

    def render_health_bars(self, screen):
        player_hp_surface = self.font.render(f"HP: {self.player.health}", True, (0, 255, 0))
        enemy_hp_surface = self.font.render(f"HP: {self.enemy.health}", True, (0, 255, 0))
        
        player_x = self.player.rect.centerx - player_hp_surface.get_width() // 2
        player_y = self.player.rect.bottom + 10
        screen.blit(player_hp_surface, (player_x, player_y))

        enemy_x = self.enemy.rect.centerx - enemy_hp_surface.get_width() // 2
        enemy_y = self.enemy.rect.top - 40
        screen.blit(enemy_hp_surface, (enemy_x, enemy_y))

    def render_characters(self, screen):
        if self.vibration_offset:
            player_rect = pygame.Rect(self.player.rect.x + self.vibration_offset, self.player.rect.y, self.player.rect.width, self.player.rect.height)
            enemy_rect = pygame.Rect(self.enemy.rect.x - self.vibration_offset, self.enemy.rect.y, self.enemy.rect.width, self.enemy.rect.height)
        else:
            player_rect = self.player.rect
            enemy_rect = self.enemy.rect

        screen.blit(self.player.image, player_rect)
        screen.blit(self.enemy.image, enemy_rect)

    def render_victory_screen(self, screen):
        victory_text = self.font.render("¡BIEN HECHO!", True, (255, 215, 0))
        text_rect = victory_text.get_rect(center=(self.game.width // 2, self.game.height // 2))
        screen.blit(victory_text, text_rect)

        if not hasattr(self, 'restart_button'):
            self.restart_button = pygame.Rect(text_rect.left - 50, text_rect.bottom + 20, 100, 30)
        
        pygame.draw.rect(screen, (0, 128, 0), self.restart_button)
        restart_text = self.font.render("REINICIAR", True, (255, 255, 255))
        screen.blit(restart_text, restart_text.get_rect(center=self.restart_button.center))

    def handle_victory_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.restart_button.collidepoint(event.pos):
                self.game.set_state('CharacterSelection')

    def update_victory(self, dt):
        pass
