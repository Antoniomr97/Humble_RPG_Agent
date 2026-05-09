from src.core.state import State

class Character:
    def __init__(self, hp, max_hp, atk, name, image):
        self.hp = hp
        self.max_hp = max_hp
        self.atk = atk
        self.name = name
        self.image = image

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def calculate_attack(self):
        import random
        return random.randint(self.atk - 5, self.atk + 5)
