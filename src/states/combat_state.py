from src.core.state import State
import pygame

class CombatState(State):
    def __init__(self, game, player_data, level=1):
        super().__init__(game)
        self.player = player_data
        self.level = level
        self.enemy = {
            'health': 20,
            'attack': 10
        }
        self.hero_x = 200
        self.enemy_x = 600
        self.y_position = 300

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Assuming 'A' key for attack
                self.attack()

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((255, 0, 0))  # Red background
        pygame.draw.rect(screen, (255, 255, 255), (self.enemy_x, self.y_position - 50, 100, 100))  # Enemy rectangle

    def attack(self):
        enemy_health = self.enemy['health'] - self.player['attack']
        print(f"Hero attacks! Enemy health: {enemy_health}")
        if enemy_health <= 0:
            print("VICTORIA")
            pygame.time.wait(2000)  # Wait for 2 seconds
            self.game.set_state(MapState(self.game, self.player, self.level))
        else:
            self.enemy['health'] = enemy_health
            self.counter_attack()

    def counter_attack(self):
        player_health = self.player['health'] - self.enemy['attack']
        print(f"Enemy attacks! Hero health: {player_health}")
        if player_health <= 0:
            print("DERROTA")
            self.game.set_state(MapState(self.game, {'health': self.player['health'], 'x': self.player['x']}, self.level))
        else:
            self.player['health'] = player_health
