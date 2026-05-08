from src.states.base_state import State

class StateManager:
    def __init__(self, state_class):
        # We pass the class and instantiate it with ourselves
        self.state_stack = [state_class(self)]

    def push_state(self, state):
        self.state_stack.append(state)

    def pop_state(self):
        if len(self.state_stack) > 1:
            return self.state_stack.pop()
        return None

    def change_state(self, state):
        """Clears stack and sets a new state"""
        self.state_stack = [state]

    def handle_events(self, event):
        if self.state_stack:
            current_state = self.state_stack[-1]
            current_state.handle_events(event)

    def update(self, dt):
        if self.state_stack:
            current_state = self.state_stack[-1]
            current_state.update(dt)

    def render(self, screen):
        if self.state_stack:
            current_state = self.state_stack[-1]
            current_state.render(screen)
