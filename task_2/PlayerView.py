from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class PlayerView:
    _jsonPlayer: dict
    name: str

    @property
    def namePlayer(self) -> str:
        return self.name

    @property
    def classPlayer(self) -> str:
        return self._jsonPlayer['class']

    @property
    def speciesPlayer(self) -> str:
        return self._jsonPlayer['species']

    @property
    def health(self) -> int:
        return self._jsonPlayer['health']

    @property
    def mana(self) -> int:
        return self._jsonPlayer['mana']

    @property
    def strength(self) -> int:
        return self._jsonPlayer['stats']['strength']

    @property
    def agility(self) -> int:
        return self._jsonPlayer['stats']['agility']

    @property
    def intelligent(self) -> int:
        return self._jsonPlayer['stats']['intelligent']

    @property
    def speed(self) -> int:
        return self._jsonPlayer['stats']['speed']

    def statsPlayerInfo(self) -> None:
        statsJson = self._jsonPlayer['stats']
        print('# Характеристики Игрока #')
        for key, value in statsJson.items():
            print(f'{key} -> {value}')
        print()

    def itemsPlayerInfo(self) -> None:
        itemJson = self._jsonPlayer['items']
        print('# Предметы игрока #')
        for i, item in enumerate(itemJson, 1):
            print(f"{i} -> {item}")
        print()

    def skillsPlayerInfo(self) -> None:
        classJson = self._jsonPlayer['skills']
        print('# Скиллы игрока #')
        for i, item in enumerate(classJson, 1):
            print(f"{i} навык -> {item}")
        print()

    def viewPlayerInfo(self) -> None:
        viewJson = self._jsonPlayer['view']
        print("# Внешность игрока #")
        for key, value in viewJson.items():
            print(f"{key} -> {value[randint(0, len(value) - 1)]}")
        print()
