import pygame
from src.core.state_machine import StateMachine

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        # Inicialización de fuentes por si acaso
        if not pygame.font.get_init():
            pygame.font.init()
            
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Humble RPG Adventure")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_machine = StateMachine()

    def set_state(self, state):
        """Cambia el estado actual del juego"""
        self.state_machine.set_state(state)

    def run(self):
        print("Bucle principal iniciado")
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if self.state_machine.current_state:
                    self.state_machine.current_state.handle_events(event)

            self.state_machine.update(dt)
            self.state_machine.render(self.screen)
            pygame.display.flip()

        pygame.quit()
