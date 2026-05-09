from src.entities.character import Character

class Hero(Character):
    def __init__(self, hp, max_hp, atk, name, image):
        super().__init__(hp, max_hp, atk, name, image)
