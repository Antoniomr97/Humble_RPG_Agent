from enum import Enum

class StateManager(Enum):
    CHARACTER_SELECTION_STATE = "CharacterSelectionState"
    MAP_STATE = "MapState"
    COMBAT_STATE = "CombatState"

    def __str__(self):
        return self.value
