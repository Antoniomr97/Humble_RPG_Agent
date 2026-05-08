import pygame

class Game:
    def __init__(self, width=800, height=600):
        print("DEBUG: pygame.init() starting")
        pygame.init()
        print("DEBUG: pygame.display.set_mode() starting")
        self.screen = pygame.display.set_mode((width, height))
        print("DEBUG: display mode set")
        pygame.display.set_caption("Humble RPG Adventure")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_manager = None

    def set_state_manager(self, state_manager):
        self.state_manager = state_manager

    def run(self):
        print("Game loop started")
        frame_count = 0
        while self.running:
            frame_count += 1
            if frame_count % 60 == 0:
                print(f"DEBUG: Frame {frame_count} rendered")
            
            dt = self.clock.tick(60) / 1000.0  # Delta time in seconds
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if self.state_manager:
                    self.state_manager.handle_events(event)

            if self.state_manager:
                self.state_manager.update(dt)
                self.state_manager.render(self.screen)

            pygame.display.flip()

        pygame.quit()
        print("Game loop ended")
