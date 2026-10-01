from enum import Enum


class ClassPlayer(Enum):
    # ====================================== #

    NONCLASS = ("Безработный", {"strength": 0, "agility": 0, "intelligent": 0, "speed": 0})
    WARLOR = ("Воин", {"strength": +5, "agility": +1, "intelligent": -1, "speed": +2})
    MAGIC = ("Маг", {"strength": -1, "agility": +1, "intelligent": +5, "speed": +1})
    BOW = ("Лучник", {"strength": -1, "agility": +5, "intelligent": 1, "speed": +3})
    FIREMAG = ("Огненный маг", {"strength": -1, "agility": +1, "intelligent": +5, "speed": +1})
    LIGHTMAG = ("Маг молний", {"strength": -1, "agility": -1, "intelligent": +5, "speed": +1})

    # ======================================= #

    def __init__(self, classname, dataclass):
        self._className = classname
        self._dataClass = dataclass

    def getTable(self) -> dict:
        return self._dataClass

    def getName(self) -> str:
        return self._className
