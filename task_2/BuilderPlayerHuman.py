from Builder import Builder
from Player import Player
from SpeciesPlayer import SpeciesPlayer
from ClassPlayer import ClassPlayer


class BuilderPlayerHuman(Builder):
    def __init__(self) -> None:
        self._PlayerClass = ClassPlayer.WARLOR
        self._PlayerSpecies = SpeciesPlayer.HUMAN
        self.reset()

    def reset(self) -> None:
        self._player = Player()

    @property
    def player(self) -> Player():
        player = self._player
        self.reset()
        return player

    def speciesPlayer(self) -> None:
        self._player.setAttribute('species', self._PlayerSpecies.getName())

    def classPlayer(self) -> None:
        self._player.setAttribute('class', self._PlayerClass.getName())

    def statsPlayer(self) -> None:
        value1 = self._PlayerClass.getTable()
        value2 = self._PlayerSpecies.getTable()

        self._player.setStateAttribute("strength", value1['strength'] + value2['strength'])
        self._player.setStateAttribute("agility", value1['agility'] + value2['agility'])
        self._player.setStateAttribute("intelligent", value1['intelligent'] + value2['intelligent'])
        self._player.setStateAttribute("speed", value1['speed'] + value2['speed'])

    def skilsPlayer(self) -> None:
        pass

    def viewPlayer(self) -> None:
        pass

    def updateSkils(self) -> None:
        pass

    def updateState(self) -> None:
        pass
