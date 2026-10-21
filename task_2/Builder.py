from abc import ABC, abstractmethod
from Player import Player
from ClassPlayer import ClassPlayer
from ItemsPlayer import ItemsPlayer
from SkillsPlayer import SkillsPlayer
from SpeciesPlayer import SpeciesPlayer
from ViewPlayer import ViewPlayer


class Builder(ABC):

    @property
    @abstractmethod
    def player(self) -> Player:
        pass

    @abstractmethod
    def removeBuilderPlayer(self):
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
    def setStrength(self, value: int):
        pass

    @abstractmethod
    def setAgility(self, value: int):
        pass

    @abstractmethod
    def setIntelligent(self, value: int):
        pass

    @abstractmethod
    def setSpeed(self, value: int):
        pass

    @abstractmethod
    def skillsPlayer(self, skillsPlayer: SkillsPlayer, number: int = 0, classPlayer: ClassPlayer = None):
        pass

    @abstractmethod
    def viewPlayer(self, view: ViewPlayer):
        pass

    @abstractmethod
    def healthPlayer(self, health: int):
        pass

    @abstractmethod
    def manaPlayer(self, mana: int):
        pass

    @abstractmethod
    def balanceStatsHealthMana(self):
        pass

    @abstractmethod
    def itemAddPlayer(self, item: str):
        pass

    @abstractmethod
    def itemAddStartPlayer(self, itemStart: ItemsPlayer):
        pass

    @abstractmethod
    def itemRemovePlayer(self):
        pass
