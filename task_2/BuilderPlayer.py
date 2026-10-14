from Builder import Builder
from Player import Player
from ClassPlayer import ClassPlayer
from SpeciesPlayer import SpeciesPlayer
from ViewPlayer import ViewPlayer
from ItemsPlayer import ItemsPlayer
from SkillsPlayer import SkillsPlayer


class BuilderPlayer(Builder):
    def __init__(self, classplayer: ClassPlayer = ClassPlayer.NONCLASS,
                 speciesplayer: SpeciesPlayer = SpeciesPlayer.HUMAN):
        self._classPlayer = classplayer
        self._speciesPlayer = speciesplayer
        self._point_stats = 20
        self._items = []
        self._skills = []
        self.reset()

    def reset(self):
        self._player = Player()

    @property
    def player(self) -> Player:
        self._player.setAttribute('items', self._items)
        player = self._player
        self.reset()
        return player

    def speciesPlayer(self, speciesplayer: SpeciesPlayer = None):
        if speciesplayer is not None:
            self._speciesPlayer = speciesplayer
        self._player.setAttribute('species', self._speciesPlayer.getName())
        return self

    def classPlayer(self, classplayer: ClassPlayer = None):
        if classplayer is not None:
            self._classPlayer = classplayer
        self._player.setAttribute('class', self._classPlayer.getName())
        return self

    def statsPlayer(self) -> None:
        if self.isCurrentClassSpecies():
            return
        value1 = self._classPlayer.getTable()
        value2 = self._speciesPlayer.getTable()

        self._player.setStateAttribute(
            "strength", value1['strength'] + value2['strength']
        ).setStateAttribute(
            "agility", value1['agility'] + value2['agility']
        ).setStateAttribute(
            "intelligent", value1['intelligent'] + value2['intelligent']
        ).setStateAttribute("speed", value1['speed'] + value2['speed'])

    def skillsPlayer(self, skillsPlayer: SkillsPlayer, number: int):
        self._skills.append(skillsPlayer[self._classPlayer.getName()][number])
        return self

    def viewPlayer(self, view: ViewPlayer, *args) -> None:
        dataView = view.buildView()
        if args is None:
            for k, v in dataView.items():
                dataView[k] = v[0]
        else:
            pass
        self._player.setAttribute('view', dataView)

    def updateSkills(self):
        pass

    def healthPlayer(self, health: int = None):
        if self.isCurrentClassSpecies():
            return
        value1 = self._classPlayer.getTable()
        value2 = self._speciesPlayer.getTable()

        if health is None:
            self._player.setAttribute("health", value1['health'] + value2['health'])
        else:
            self._player.setAttribute("health", value1['health'] + value2['health'] + health)

        return self

    def manaPlayer(self, mana: int = None):
        if self.isCurrentClassSpecies():
            return
        value1 = self._classPlayer.getTable()
        value2 = self._speciesPlayer.getTable()

        if mana is None:
            self._player.setAttribute("mana", value1['mana'] + value2['mana'])
        else:
            self._player.setAttribute("mana", value1['mana'] + value2['mana'] + mana)

        return self

    def isCurrentClassSpecies(self) -> bool:
        return self._classPlayer is None and self._speciesPlayer is None

    def balanceHealthMana(self):
        health, mana = self._player.getHealthManaPlayer()
        self.healthPlayer(1 if health < 0 else health)
        self.manaPlayer(1 if mana < 0 else mana)

        return self

    def itemAddPlayer(self, item: str):
        self._items.append(item)
        return self

    def itemAddStartPlayer(self, itemStart: ItemsPlayer):
        for item in itemStart.getItems():
            self._items.append(item)

    def itemRemovePlayer(self):
        self._items.remove(self._items[-1])
        return self
