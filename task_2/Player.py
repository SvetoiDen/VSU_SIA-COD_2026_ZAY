from typing import Any
from json import dump, dumps
from random import randint


class Player:
    def __init__(self) -> None:
        self._pointStats = 20
        self._jsonPlayer = {
            "species": None,
            "class": None,
            "health": 20,
            "mana": 20,
            "stats": {
                "strength": 1,
                "agility": 1,
                "intelligent": 1,
                "speed": 1
            },
            "skills": None,
            "items": None,
            "view": None
        }

    def setAttribute(self, key: str, value: Any):
        self._jsonPlayer[key] = value
        return self

    def setStateAttribute(self, state: str, value: int):
        self._jsonPlayer['stats'][state] += value
        return self

    def getHealthManaPlayer(self) -> tuple[int, int]:
        return self._jsonPlayer['health'], self._jsonPlayer['mana']

    def _isCheckPoint(self) -> bool:
        point = self._jsonPlayer['stats']['strength'] + self._jsonPlayer['stats']['agility'] + \
                self._jsonPlayer['stats']['intelligent'] + self._jsonPlayer['stats']['speed']
        return self._pointStats - point < 0

    def _viewPlayer(self, jsData: dict) -> None:
        print(dumps(jsData, indent=2, ensure_ascii=False))

    def _saveFilePlayer(self, jsData: dict, path: str = "D:/Cogs_Project/VSU_SIA-COD_2026_ZAY/task_2") -> None:
        with open(f'{path}/person_{randint(1, 10 ** 3)}.json', 'w', encoding='utf-8') as jFile:
            dump(jsData, jFile, indent=3, ensure_ascii=False)

    def build(self) -> dict:
        if self._isCheckPoint():
            raise Exception(f"Очки навыков превышают допустимые малые значения -> {self._jsonPlayer['stats']}")
        self._viewPlayer(self._jsonPlayer)
        # self._saveFilePlayer(self._jsonPlayer)
        return {200: "correct"}
