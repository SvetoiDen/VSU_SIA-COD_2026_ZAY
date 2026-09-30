from enum import Enum


class ClassPlayer(Enum):
    # ====================================== #

    WARLOR = ("Воин", {})
    MAGIC = ("Маг", {})
    BOW = ("Лучник", {})
    FIREMAG = ("Огненный маг", {})
    LIGHTMAG = ("Маг молний", {})

    # ======================================= #

    def __init__(self, classname, dataclass):
        self._className = classname
        self._dataClass = dataclass

    def getTable(self) -> dict:
        return self._dataClass

    def getName(self) -> str:
        return self._className
