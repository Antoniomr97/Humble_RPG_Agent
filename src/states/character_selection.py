import pygame
from src.core.state import State

class CharacterSelectionState(State):
    def __init__(self, game):
        self.game = game
        self.heroes = [
            {"name": "Vermillion", "path": "assets/sprites/heroes/Vermillion/ImagenBase/PJ_Vermillion.png", "stats": "HP: 50 | ATK: 15"},
            {"name": "Gandall", "path": "assets/sprites/heroes/Gandall/ImagenBase/PJ_Gandall.png", "stats": "HP: 40 | ATK: 30"},
            {"name": "Backnister", "path": "assets/sprites/heroes/Backnister/ImagenBase/PJ_Backnister.png", "stats": "HP: 70 | ATK: 20"}
        ]
        self.selected = 0
        # Carga segura de imágenes
        self.hero_images = []
        for h in self.heroes:
            try:
                img = pygame.image.load(h["path"]).convert_alpha()
                self.hero_images.append(img)
            except Exception as e:
                print(f"Error cargando imagen {h['path']}: {e}")
                # Placeholder si falla la carga
                surf = pygame.Surface((180, 180))
                surf.fill((100, 100, 100))
                self.hero_images.append(surf)
        
        self.font = pygame.font.Font(None, 36)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selected = (self.selected - 1) % len(self.heroes)
            elif event.key == pygame.K_RIGHT:
                self.selected = (self.selected + 1) % len(self.heroes)
            elif event.key == pygame.K_RETURN:
                from src.states.map_state import MapState
                selected_hero = self.heroes[self.selected].copy()
                selected_hero["image"] = self.hero_images[self.selected]
                self.game.set_state(MapState(self.game, selected_hero))

    def render(self, screen):
        screen.fill((0, 0, 0)) # Fondo retro negro
        for i, hero in enumerate(self.heroes):
            x = 100 + i * 250
            y = 200
            
            # Nombre resaltado
            color = (255, 255, 0) if i == self.selected else (255, 255, 255)
            name_surf = self.font.render(hero["name"], True, color)
            screen.blit(name_surf, (x + 90 - name_surf.get_width()//2, y - 50))
            
            # Imagen con marco si está seleccionada
            if i == self.selected:
                pygame.draw.rect(screen, (255, 255, 0), (x-5, y-5, 190, 190), 3)
            
            screen.blit(pygame.transform.scale(self.hero_images[i], (180, 180)), (x, y))
            
            # Cuadro de stats
            pygame.draw.rect(screen, (255, 255, 255), (x, y + 200, 180, 60), 2)
            stats_surf = self.font.render(hero["stats"], True, (255, 255, 255))
            screen.blit(stats_surf, (x + 10, y + 215))

    def update(self, dt):
        pass
