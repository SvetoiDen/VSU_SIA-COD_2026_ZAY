from typing import Any


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
            "skils": None,
            "items": None,
            "view": None
        }

    def setAttribute(self, key: str, value: Any):
        self._jsonPlayer[key] = value
        return self

    def setStateAttribute(self, state: str, value: int):
        self._pointStats -= value
        self._jsonPlayer['stats'][state] += value
        return self

    def isCheckPoint(self) -> bool:
        return self._pointStats < 0

    def getHealthManaPlayer(self) -> tuple[int, int]:
        return self._jsonPlayer['health'], self._jsonPlayer['mana']

    def build(self) -> dict:
        if self.isCheckPoint():
            return {"error": 404}
        return self._jsonPlayer
