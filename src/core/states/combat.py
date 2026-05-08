from src.core.state import State

class CombatState(State):
    def enter(self):
        print("Entering Combat")

    def exit(self):
        print("Exiting Combat")

    def update(self, dt):
        # Update logic for combat state
        pass

    def render(self, screen):
        # Render the combat screen
        screen.fill((0, 0, 255))  # Fill the screen with blue
