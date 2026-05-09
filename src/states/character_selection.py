import pygame
from src.core.state import State

class CharacterSelectionState(State):
    def __init__(self, game):
        self.game = game
        # Usamos TUS rutas reales y tus personajes
        self.heroes = [
            {"name": "Vermillion", "path": "assets/sprites/heroes/Vermillion/ImagenBase/PJ_Vermillion.png", "hp": 50, "atk": 15},
            {"name": "Gandall", "path": "assets/sprites/heroes/Gandall/ImagenBase/PJ_Gandall.png", "hp": 40, "atk": 30},
            {"name": "Backnister", "path": "assets/sprites/heroes/Backnister/ImagenBase/PJ_Backnister.png", "hp": 70, "atk": 20}
        ]
        self.hero_images = []
        for h in self.heroes:
            try:
                img = pygame.image.load(h["path"]).convert_alpha()
                self.hero_images.append(pygame.transform.scale(img, (180, 180)))
            except Exception as e:
                print(f"Error cargando {h['path']}: {e}")
                surf = pygame.Surface((180, 180))
                surf.fill((100, 100, 100))
                self.hero_images.append(surf)
        
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
                    hero_data = self.heroes[i].copy()
                    hero_data["image"] = self.hero_images[i]
                    self.game.set_state(MapState(self.game, hero_data))

    def render(self, screen):
        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        column_width = screen.get_width() // 3

        for i, hero in enumerate(self.heroes):
            # 1. Cálculo de posición centrada
            x = (column_width * i) + (column_width // 2) - 90
            y = 200
            char_rect = pygame.Rect(x, y, 180, 180)

            # 2. Nombre arriba
            name_txt = self.font.render(hero["name"], True, (255, 255, 255))
            screen.blit(name_txt, (x + 90 - name_txt.get_width()//2, y - 40))

            # 3. Imagen del héroe
            screen.blit(self.hero_images[i], (x, y))

            # 4. EFECTO HOVER (Borde amarillo solo si el ratón está encima)
            if char_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 0), char_rect, 3)

            # 5. Caja de Stats (Valores centrados)
            stats_rect = pygame.Rect(x, y + 190, 180, 60)
            pygame.draw.rect(screen, (255, 255, 255), stats_rect, 2)
            
            hp_txt = self.font.render(f"HP: {hero['hp']}", True, (200, 200, 200))
            atk_txt = self.font.render(f"ATK: {hero['atk']}", True, (200, 200, 200))
            
            screen.blit(hp_txt, (stats_rect.centerx - hp_txt.get_width()//2, stats_rect.y + 10))
            screen.blit(atk_txt, (stats_rect.centerx - atk_txt.get_width()//2, stats_rect.y + 35))
