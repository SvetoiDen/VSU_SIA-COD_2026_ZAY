from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class PlayerView:
    jsonPlayer: dict
    name: str

    @property
    def namePlayer(self) -> str:
        return self.name

    @property
    def classPlayer(self) -> str:
        return self.jsonPlayer['class']

    @property
    def speciesPlayer(self) -> str:
        return self.jsonPlayer['species']

    @property
    def health(self) -> int:
        return self.jsonPlayer['health']

    @property
    def mana(self) -> int:
        return self.jsonPlayer['mana']

    @property
    def strength(self) -> int:
        return self.jsonPlayer['stats']['strength']

    @property
    def agility(self) -> int:
        return self.jsonPlayer['stats']['agility']

    @property
    def intelligent(self) -> int:
        return self.jsonPlayer['stats']['intelligent']

    @property
    def speed(self) -> int:
        return self.jsonPlayer['stats']['speed']

    def statsPlayerInfo(self) -> None:
        statsJson = self.jsonPlayer['stats']
        print('# Характеристики Игрока #')
        for key, value in statsJson.items():
            print(f'{key} -> {value}')
        print()

    def itemsPlayerInfo(self) -> None:
        itemJson = self.jsonPlayer['items']
        print('# Предметы игрока #')
        for i, item in enumerate(itemJson, 1):
            print(f"{i} -> {item}")
        print()

    def skillsPlayerInfo(self) -> None:
        classJson = self.jsonPlayer['skills']
        print('# Скиллы игрока #')
        for i, item in enumerate(classJson, 1):
            print(f"{i} навык -> {item}")
        print()

    def viewPlayerInfo(self) -> None:
        viewJson = self.jsonPlayer['view']
        print("# Внешность игрока #")
        for key, value in viewJson.items():
            print(f"{key} -> {value[randint(0, len(value)-1)]}")
        print()
