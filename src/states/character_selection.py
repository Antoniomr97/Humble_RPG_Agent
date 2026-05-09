import pygame
from src.core.state import State
from src.entities.hero import Hero

class CharacterSelectionState(State):
    def __init__(self, game):
        super().__init__(game)
        # Cargamos los héroes usando la nueva clase
        self.heroes = [
            Hero(hp=50, max_hp=50, atk=15, name="Vermillion", image=None),
            Hero(hp=40, max_hp=40, atk=30, name="Gandall", image=None),
            Hero(hp=70, max_hp=70, atk=20, name="Backnister", image=None)
        ]
        
        # Paths reales de los sprites
        self.hero_paths = [
            "assets/sprites/heroes/Vermillion/ImagenBase/PJ_Vermillion.png",
            "assets/sprites/heroes/Gandall/ImagenBase/PJ_Gandall.png",
            "assets/sprites/heroes/Backnister/ImagenBase/PJ_Backnister.png"
        ]
        
        self.hero_images = []
        for i, h in enumerate(self.heroes):
            try:
                img = pygame.image.load(self.hero_paths[i]).convert_alpha()
                self.hero_images.append(pygame.transform.scale(img, (180, 180)))
                h.image = self.hero_images[-1] # Guardamos la imagen en el objeto Hero
            except:
                surf = pygame.Surface((180, 180))
                surf.fill((100, 100, 100))
                self.hero_images.append(surf)
                h.image = surf
        
        self.font = pygame.font.Font(None, 32)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            column_width = 800 // 3
            for i in range(len(self.heroes)):
                x = (column_width * i) + (column_width // 2) - 90
                rect = pygame.Rect(x, 200, 180, 180)
                if rect.collidepoint(mouse_pos):
                    from src.states.map_state import MapState
                    self.game.set_state(MapState(self.game, self.heroes[i]))

    def render(self, screen):
        screen.fill((10, 10, 20)) # Fondo oscuro elegante
        mouse_pos = pygame.mouse.get_pos()
        column_width = screen.get_width() // 3

        title = self.font.render("SELECCIONA TU HÉROE", True, (255, 255, 255))
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 50))

        for i, hero in enumerate(self.heroes):
            x = (column_width * i) + (column_width // 2) - 90
            y = 200
            char_rect = pygame.Rect(x, y, 180, 180)

            # Nombre
            name_txt = self.font.render(hero.name, True, (255, 255, 255))
            screen.blit(name_txt, (x + 90 - name_txt.get_width()//2, y - 40))

            # Imagen
            screen.blit(self.hero_images[i], (x, y))

            # Hover
            if char_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 0), char_rect, 3)

            # Stats
            stats_rect = pygame.Rect(x, y + 190, 180, 60)
            pygame.draw.rect(screen, (255, 255, 255), stats_rect, 2)
            hp_txt = self.font.render(f"HP: {hero.hp}", True, (200, 200, 200))
            atk_txt = self.font.render(f"ATK: {hero.atk}", True, (200, 200, 200))
            screen.blit(hp_txt, (stats_rect.centerx - hp_txt.get_width()//2, stats_rect.y + 10))
            screen.blit(atk_txt, (stats_rect.centerx - atk_txt.get_width()//2, stats_rect.y + 35))
