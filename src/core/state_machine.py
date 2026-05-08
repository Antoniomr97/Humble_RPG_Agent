class StateMachine:
    def __init__(self):
        self.current_state = None

    def set_state(self, state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = state
        self.current_state.enter()

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)

    def render(self, screen):
        if self.current_state:
            self.current_state.render(screen)
