class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
