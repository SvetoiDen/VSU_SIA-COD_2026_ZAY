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
        self._player.setAttribute('skills', self._skills)
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

    def setStrength(self, value: int = 0):
        if value < 0:
            raise Exception("Значение параметра силы не может быть меньше 0")
        self._player.setStateAttribute('strength', value)

    def setAgility(self, value: int):
        if value < 0:
            raise Exception("Значение параметра ловкости не может быть меньше 0")
        self._player.setStateAttribute('agility', value)

    def setIntelligent(self, value: int):
        if value < 0:
            raise Exception("Значение параметра интеллекта не может быть меньше 0")
        self._player.setStateAttribute('intelligent', value)

    def setSpeed(self, value: int):
        if value < 0:
            raise Exception("Значение параметра скорости не может быть меньше 0")
        self._player.setStateAttribute('speed', value)

    def skillsPlayer(self, skillsPlayer: SkillsPlayer, number: int = 0, classPlayer: ClassPlayer = None):
        if number >= 10:
            raise Exception("Нумерация скиллов от 0 до 9")

        if skillsPlayer == SkillsPlayer.NON_SKILL:
            self._skills.append(skillsPlayer.getSkillClass(ClassPlayer.NONCLASS, number))
        else:
            if classPlayer is None:
                skillClass = skillsPlayer.getSkillClass(self._classPlayer, number)
            else:
                skillClass = skillsPlayer.getSkillClass(classPlayer, number)

            if skillClass is None:
                raise Exception("Такой скилл у класса не найден")
            self._skills.append(skillsPlayer.getSkillClass(self._classPlayer, number))
        return self

    def viewPlayer(self, view: ViewPlayer, *args) -> None:
        dataView = view.buildView()
        if args is None:
            for k, v in dataView.items():
                dataView[k] = v[0]
        else:
            pass
        self._player.setAttribute('view', dataView)

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

    def balanceStatsHealthMana(self):
        health, mana = self._player.getHealthManaPlayer()
        self.healthPlayer(1 if health < 0 else health)
        self.manaPlayer(1 if mana < 0 else mana)
        self.statsPlayer()

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
