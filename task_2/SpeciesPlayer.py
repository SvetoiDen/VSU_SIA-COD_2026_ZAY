from enum import Enum


class SpeciesPlayer(Enum):
    # ====================================== #

    HUMAN = ("Человек", {})
    ELF = ("Эльф", {})
    DFARF = ("Дварф", {})
    COBOLT = ("Кобольт", {})
    ORC = ("Орк", {})

    # ====================================== #

    def __init__(self, speciesname, dataspecies):
        self._speciesName = speciesname
        self._dataSpecies = dataspecies

    def getTable(self) -> dict:
        return self._dataSpecies

    def getName(self) -> str:
        return self._speciesName
