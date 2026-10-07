from enum import Enum


class ClassPlayer(Enum):
    # ====================================== #

    NONCLASS = (
        "Безработный",
        {"strength": 0, "agility": 0, "intelligent": 0, "speed": 0, 'health': 0, 'mana': 0})
    WARLOR = (
        "Воин",
        {"strength": +5, "agility": +1, "intelligent": -1, "speed": +2, 'health': +20, 'mana': -15})
    MAGIC = (
        "Маг",
        {"strength": -1, "agility": +1, "intelligent": +5, "speed": +1, 'health': -15, 'mana': +20})
    BOW = (
        "Лучник",
        {"strength": -1, "agility": +5, "intelligent": 1, "speed": +3, 'health': +5, 'mana': +5})
    FIREMAG = (
        "Огненный маг",
        {"strength": -1, "agility": +1, "intelligent": +5, "speed": +1, 'health': -15, 'mana': +20})
    LIGHTMAG = (
        "Маг молний",
        {"strength": -1, "agility": -1, "intelligent": +5, "speed": +1, 'health': -15, 'mana': +20})
    ROGUE = (
        "Разбойник",
        {"strength": +1, "agility": +5, "intelligent": +2, "speed": +4, "health": -5, "mana": 0}
    )

    PALADIN = (
        "Паладин",
        {"strength": +4, "agility": -1, "intelligent": +2, "speed": 0, "health": +15, "mana": +5}
    )

    CLERIC = (
        "Жрец",
        {"strength": 0, "agility": -1, "intelligent": +4, "speed": 0, "health": +5, "mana": +15}
    )

    NECROMANCER = (
        "Некромант",
        {"strength": -2, "agility": 0, "intelligent": +5, "speed": -1, "health": -10, "mana": +25}
    )

    DRUID = (
        "Друид",
        {"strength": +1, "agility": +1, "intelligent": +3, "speed": +1, "health": +5, "mana": +15}
    )

    BARBARIAN = (
        "Варвар",
        {"strength": +6, "agility": -1, "intelligent": -3, "speed": +1, "health": +25, "mana": -20}
    )

    MONK = (
        "Монах",
        {"strength": +2, "agility": +3, "intelligent": +1, "speed": +4, "health": +10, "mana": +5}
    )

    ASSASSIN = (
        "Ассасин",
        {"strength": +2, "agility": +6, "intelligent": +1, "speed": +5, "health": -10, "mana": -5}
    )

    BARD = (
        "Бард",
        {"strength": -1, "agility": +3, "intelligent": +3, "speed": +2, "health": 0, "mana": +10}
    )

    SUMMONER = (
        "Призыватель",
        {"strength": -2, "agility": 0, "intelligent": +6, "speed": 0, "health": -10, "mana": +25}
    )

    ICE_MAG = (
        "Ледяной маг",
        {"strength": -1, "agility": +1, "intelligent": +5, "speed": 0, "health": -10, "mana": +20}
    )

    EARTH_MAG = (
        "Маг земли",
        {"strength": +1, "agility": -1, "intelligent": +4, "speed": -1, "health": +10, "mana": +15}
    )

    # ======================================= #

    def __init__(self, classname, dataclass):
        self._className = classname
        self._dataClass = dataclass

    def getTable(self) -> dict:
        return self._dataClass

    def getName(self) -> str:
        return self._className
