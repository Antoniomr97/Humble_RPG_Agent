from src.core.state import State

class CharacterSelectionState(State):
    def enter(self):
        print("Entering Character Selection")

    def exit(self):
        print("Exiting Character Selection")

    def update(self, dt):
        # Update logic for character selection
        pass

    def render(self, screen):
        # Render the character selection screen
        screen.fill((255, 0, 0))  # Fill the screen with red
