from enum import Enum


class SpeciesPlayer(Enum):
    # ====================================== #

    HUMAN = ("Человек", {"strength": 0, "agility": 0, "intelligent": 0, "speed": 0, 'health': -10, 'mana': -10})
    HUMAN_WITH_MAGIC = ("Человек, предосположенный к магии", {"strength": 0, "agility": 0, "intelligent": +3, "speed": 0, 'health': -15, 'mana': +15})
    ELF = ("Эльф", {"strength": -1, "agility": +3, "intelligent": +2, "speed": +2, 'health': 0, 'mana': 0})
    DFARF = ("Дварф", {"strength": +5, "agility": -1, "intelligent": -1, "speed": -1, 'health': +5, 'mana': -20})
    COBOLT = ("Кобольт", {"strength": +1, "agility": +2, "intelligent": +2, "speed": +4, 'health': +5})
    ORC = ("Орк", {"strength": +8, "agility": -3, "intelligent": -5, "speed": -2, 'health': +20, 'mana': -40})

    # ====================================== #

    def __init__(self, speciesname, dataspecies):
        self._speciesName = speciesname
        self._dataSpecies = dataspecies

    def getTable(self) -> dict:
        return self._dataSpecies

    def getName(self) -> str:
        return self._speciesName
