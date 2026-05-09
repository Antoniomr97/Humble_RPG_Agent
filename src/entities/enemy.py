from src.entities.character import Character
import random

class Enemy(Character):
    ENEMIES_POOL = [
        {"name": "Trasgo", "hp": 50, "max_hp": 50, "atk": 10, "image": None},
        {"name": "Orco", "hp": 60, "max_hp": 60, "atk": 12, "image": None},
        {"name": "Esqueleto", "hp": 40, "max_hp": 40, "atk": 8, "image": None},
        {"name": "Slime", "hp": 30, "max_hp": 30, "atk": 6, "image": None}
    ]

    def __init__(self):
        enemy_data = random.choice(self.ENEMIES_POOL)
        super().__init__(
            hp=enemy_data["hp"],
            max_hp=enemy_data["max_hp"],
            atk=enemy_data["atk"],
            name=enemy_data["name"],
            image=self._get_image(enemy_data["name"])
        )

    def _get_image(self, enemy_name):
        if enemy_name == "Trasgo":
            return (0, 255, 0)  # Green
        elif enemy_name == "Orco":
            return (192, 192, 192)  # Gray
        elif enemy_name == "Esqueleto":
            return (255, 255, 255)  # White
        elif enemy_name == "Slime":
            return (0, 0, 255)  # Blue
