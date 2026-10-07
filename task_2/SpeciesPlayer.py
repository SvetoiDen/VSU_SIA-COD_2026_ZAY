from enum import Enum


class SpeciesPlayer(Enum):
    # ====================================== #

    HUMAN = (
        "Человек",
        {"strength": 0, "agility": 0, "intelligent": 0, "speed": 0, "health": -10, "mana": -10}
    )

    HUMAN_WITH_MAGIC = (
        "Человек, предрасположенный к магии",
        {"strength": 0, "agility": 0, "intelligent": +3, "speed": 0, "health": -15, "mana": +15}
    )

    ELF = (
        "Эльф",
        {"strength": -1, "agility": +3, "intelligent": +2, "speed": +2, "health": 0, "mana": 0}
    )

    DFARF = (
        "Дварф",
        {"strength": +5, "agility": -1, "intelligent": -1, "speed": -1, "health": +5, "mana": -20}
    )

    COBOLT = (
        "Кобольт",
        {"strength": +1, "agility": +2, "intelligent": +2, "speed": +4, "health": +5, "mana": 0}
    )

    ORC = (
        "Орк",
        {"strength": +8, "agility": -3, "intelligent": -5, "speed": -2, "health": +20, "mana": -40}
    )

    HALFLING = (
        "Полурослик",
        {"strength": -2, "agility": +4, "intelligent": +1, "speed": +3, "health": +5, "mana": 0}
    )

    GNOME = (
        "Гном",
        {"strength": -1, "agility": +2, "intelligent": +4, "speed": +1, "health": -5, "mana": +10}
    )

    TIEFLING = (
        "Тифлинг",
        {"strength": 0, "agility": +1, "intelligent": +2, "speed": +1, "health": 0, "mana": +10}
    )

    DRAGONBORN = (
        "Драконорождённый",
        {"strength": +5, "agility": 0, "intelligent": +1, "speed": -1, "health": +15, "mana": +5}
    )

    GOBLIN = (
        "Гоблин",
        {"strength": -1, "agility": +4, "intelligent": +1, "speed": +3, "health": -5, "mana": 0}
    )

    CATFOLK = (
        "Кошачий народ",
        {"strength": +1, "agility": +5, "intelligent": 0, "speed": +4, "health": 0, "mana": 0}
    )

    LIZARDFOLK = (
        "Ящеролюд",
        {"strength": +3, "agility": +2, "intelligent": 0, "speed": +1, "health": +10, "mana": -5}
    )

    FAIRY = (
        "Фея",
        {"strength": -5, "agility": +4, "intelligent": +3, "speed": +5, "health": -20, "mana": +25}
    )

    UNDEAD = (
        "Нежить",
        {"strength": +2, "agility": -2, "intelligent": +1, "speed": -2, "health": +15, "mana": +10}
    )

    DEMON = (
        "Демон",
        {"strength": +4, "agility": +1, "intelligent": +2, "speed": 0, "health": +10, "mana": +15}
    )

    ANGEL = (
        "Ангел",
        {"strength": +1, "agility": +1, "intelligent": +4, "speed": +2, "health": 0, "mana": +20}
    )

    TROLL = (
        "Тролль",
        {"strength": +7, "agility": -3, "intelligent": -4, "speed": -2, "health": +25, "mana": -30}
    )

    CENTAUR = (
        "Кентавр",
        {"strength": +3, "agility": +2, "intelligent": 0, "speed": +5, "health": +10, "mana": -5}
    )

    # ====================================== #

    def __init__(self, speciesname, dataspecies):
        self._speciesName = speciesname
        self._dataSpecies = dataspecies

    def getTable(self) -> dict:
        return self._dataSpecies

    def getName(self) -> str:
        return self._speciesName
