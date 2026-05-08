from src.core.state import State

class MapState(State):
    def enter(self):
        print("Entering Map")

    def exit(self):
        print("Exiting Map")

    def update(self, dt):
        # Update logic for map state
        pass

    def render(self, screen):
        # Render the map screen
        screen.fill((0, 255, 0))  # Fill the screen with green
