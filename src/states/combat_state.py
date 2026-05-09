from src.core.engine import Game
from src.core.state import State

class CombatState(State):
    def __init__(self, game: Game):
        super().__init__(game)
        self.options = ["ATACAR", "DEFENDER"]
        self.selected_option_index = 0
        self.font = pygame.font.Font(None, 36)
        self.back_button_rect = pygame.Rect(50, 50, 120, 40)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.selected_option_index > 0:
                self.selected_option_index -= 1
            elif event.key == pygame.K_DOWN and self.selected_option_index < len(self.options) - 1:
                self.selected_option_index += 1
            elif event.key == pygame.K_RETURN:
                self.execute_selected_option()
        elif event.type == pygame.MOUSEBUTTONDOWN and self.back_button_rect.collidepoint(event.pos):
            self.game.set_state(MapState(self.game))

    def update(self, dt):
        pass

    def render(self, screen):
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255) if i == self.selected_option_index else (128, 128, 128))
            screen.blit(text, (100, 100 + i * 40))

        pygame.draw.rect(screen, (0, 255, 0), self.back_button_rect)
        back_text = self.font.render("VOLVER", True, (0, 0, 0))
        screen.blit(back_text, (self.back_button_rect.centerx - back_text.get_width() // 2, self.back_button_rect.centery - back_text.get_height() // 2))

    def execute_selected_option(self):
        if self.options[self.selected_option_index] == "ATACAR":
            print("Héroe ataca con [ATK] de daño")
        elif self.options[self.selected_option_index] == "DEFENDER":
            print("Héroe se defiende: daño recibido reducido al 50%")
