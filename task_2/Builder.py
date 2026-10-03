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
    def speciesPlayer(self, speciesPlayer: SpeciesPlayer = None):
        pass

    @abstractmethod
    def classPlayer(self, classPlayer: ClassPlayer):
        pass

    @abstractmethod
    def statsPlayer(self):
        pass

    @abstractmethod
    def skilsPlayer(self):
        pass

    @abstractmethod
    def viewPlayer(self):
        pass

    @abstractmethod
    def updateSkils(self) -> None:
        pass

    @abstractmethod
    def updateState(self) -> None:
        pass

    @abstractmethod
    def healthPlayer(self, health: int):
        pass

    @abstractmethod
    def manaPlayer(self, mana: int):
        pass

    @abstractmethod
    def balanceHealthMana(self):
        pass