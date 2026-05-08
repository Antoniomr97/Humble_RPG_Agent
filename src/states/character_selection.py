import pygame
from pygame.locals import *
from src.states.base_state import State
from src.states.map import MapState

class CharacterSelectionState(State):
    def __init__(self, manager):
        super().__init__(manager)
        self.colors = {
            'Vermillion (Picaro)': (255, 69, 0),
            'Backnister (Guerrero)': (221, 160, 221),
            'Gandall (Mago)': (0, 139, 139)
        }
        self.stats = {
            'Vermillion (Picaro)': {'Vida': 50, 'Ataque': 15},
            'Backnister (Guerrero)': {'Vida': 70, 'Ataque': 20},
            'Gandall (Mago)': {'Vida': 40, 'Ataque': 30}
        }
        self.character_rects = []
        self.initialized_rects = False

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for rect, name in self.character_rects:
                if rect.collidepoint(event.pos):
                    print(f"Selected: {name}")
                    # Transition to MapState, passing the stats
                    self.manager.change_state(MapState(self.manager, self.stats[name]))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((30, 30, 30))
        width, height = screen.get_size()
        
        # Clear rects to redefine them (or just do it once)
        if not self.initialized_rects:
            self.character_rects = []
            
        for i, (name, color) in enumerate(self.colors.items()):
            # Calculate position
            rect_width = 200
            rect_height = 200
            spacing = (width - (rect_width * 3)) // 4
            x = spacing + i * (rect_width + spacing)
            y = (height // 2) - 150
            
            char_rect = pygame.Rect(x, y, rect_width, rect_height)
            if not self.initialized_rects:
                self.character_rects.append((char_rect, name))
            
            # Draw character square
            pygame.draw.rect(screen, color, char_rect)
            
            # Draw name and stats below
            font = pygame.font.Font(None, 24)
            name_surf = font.render(name, True, (255, 255, 255))
            screen.blit(name_surf, (x, y + rect_height + 10))
            
            stat_text = f"HP: {self.stats[name]['Vida']} | ATK: {self.stats[name]['Ataque']}"
            stats_surf = font.render(stat_text, True, (200, 200, 200))
            screen.blit(stats_surf, (x, y + rect_height + 40))
            
        self.initialized_rects = True
