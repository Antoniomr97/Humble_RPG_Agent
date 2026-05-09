from src.core.state_manager import StateManager
from src.core.engine import Game
import pygame

class CharacterSelectionState(State):
    def __init__(self, game):
        super().__init__(game)
        self.heroes = [
            {"name": "Vermillion", "image_path": "assets/sprites/heroes/Vermillion/ImagenBase/PJ_Vermillion.png"},
            {"name": "Gandall", "image_path": "assets/sprites/heroes/Gandall/ImagenBase/PJ_Gandall.png"},
            {"name": "Backnister", "image_path": "assets/sprites/heroes/Backnister/ImagenBase/PJ_Backnister.png"}
        ]
        self.selected_index = 0
        self.hero_images = [pygame.image.load(hero["image_path"]).convert_alpha() for hero in self.heroes]
        self.font = pygame.font.Font(None, 36)
        self.background_color = (0, 0, 0)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = max(0, self.selected_index - 1)
            elif event.key == pygame.K_DOWN:
                self.selected_index = min(len(self.heroes) - 1, self.selected_index + 1)
            elif event.key == pygame.K_ESCAPE:
                self.game.set_state(StateManager.MAP_STATE)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(self.background_color)
        for i, hero in enumerate(self.heroes):
            text = self.font.render(hero["name"], True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, 100 + i * 100))
            screen.blit(text, text_rect)
            hero_image_rect = self.hero_images[i].get_rect(center=(screen.get_width() // 2, 300 + i * 100))
            screen.blit(self.hero_images[i], hero_image_rect)
        
        pygame.display.flip()

    def get_selected_hero(self):
        return self.heroes[self.selected_index]
