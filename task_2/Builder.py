from abc import ABC, abstractmethod
from Player import Player
from ClassPlayer import ClassPlayer
from SpeciesPlayer import SpeciesPlayer


class Builder(ABC):

    @property
    @abstractmethod
    def player(self) -> Player:
        pass

    @abstractmethod
    def speciesPlayer(self) -> None:
        pass

    @abstractmethod
    def classPlayer(self) -> None:
        pass

    @abstractmethod
    def statsPlayer(self) -> None:
        pass

    @abstractmethod
    def skilsPlayer(self) -> None:
        pass

    @abstractmethod
    def viewPlayer(self) -> None:
        pass

    @abstractmethod
    def updateSkils(self) -> None:
        pass

    @abstractmethod
    def updateState(self) -> None:
        pass

    @abstractmethod
    def setClassPlayer(self, classplayer: ClassPlayer) -> None:
        pass

    @abstractmethod
    def setSpeciesPlayer(self, speciesplayer: SpeciesPlayer) -> None:
        pass

    @abstractmethod
    def healthPlayer(self, health: int):
        pass

    @abstractmethod
    def manaPlayer(self, mana: int):
        pass