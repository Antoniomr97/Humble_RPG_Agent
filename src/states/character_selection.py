from src.core.state import State
import pygame

class CharacterSelection(State):
    def __init__(self, game):
        super().__init__(game)
        self.characters = [
            {"image": pygame.image.load("assets/heroes/warrior.png"), "name": "Warrior", "hp": 100, "atk": 20},
            {"image": pygame.image.load("assets/heroes/mage.png"), "name": "Mage", "hp": 80, "atk": 30},
            {"image": pygame.image.load("assets/heroes/rogue.png"), "name": "Rogue", "hp": 70, "atk": 25}
        ]
        self.selected_char = None

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, char in enumerate(self.characters):
                char_rect = pygame.Rect(char["x"] - 10, char["y"] + char["image"].get_height() + 10, char["image"].get_width() + 20, 30)
                if char_rect.collidepoint(mouse_pos):
                    self.selected_char = i
                    self.game.change_state(MapState(self.game))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        column_width = screen.get_width() // 3
        for i, char in enumerate(self.characters):
            char["x"] = (column_width * i) + (column_width // 2) - (char["image"].get_width() // 2)
            char["y"] = screen.get_height() // 2 - char["image"].get_height() // 2

            # Draw character image
            screen.blit(char["image"], (char["x"], char["y"]))

            # Calculate stats box position and draw
            stats_box_y = char["y"] + char["image"].get_height() + 10
            pygame.draw.rect(screen, (255, 255, 255), (char["x"] - 10, stats_box_y, char["image"].get_width() + 20, 30))

            # Draw text centered in the stats box with padding
            font = pygame.font.Font(None, 24)
            hp_text = font.render(f"HP: {char['hp']}", True, (0, 0, 0))
            atk_text = font.render(f"ATK: {char['atk']}", True, (0, 0, 0))
            screen.blit(hp_text, (char["x"] + 5, stats_box_y + 2))
            screen.blit(atk_text, (char["x"] + 5, stats_box_y + 18))

            # Draw yellow border on hover
            mouse_pos = pygame.mouse.get_pos()
            char_rect = pygame.Rect(char["x"] - 10, char["y"] + char["image"].get_height() + 10, char["image"].get_width() + 20, 30)
            if char_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 0), char_rect, 3)

# Placeholder for MapState
class MapState(State):
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((0, 128, 0))  # Example green background for MapState
