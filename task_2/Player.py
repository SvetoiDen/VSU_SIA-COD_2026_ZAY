from typing import Any


class Player:
    def __init__(self) -> None:
        self._pointStats = 20
        self._jsonPlayer = {
            "species": None,
            "class": None,
            "health": 20,
            "manapool": 20,
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

    def setAttribute(self, key: str, value: Any) -> None:
        self._jsonPlayer[key] = value

    def setStateAttribute(self, state: str, value: int) -> None:
        self._pointStats -= value
        self._jsonPlayer['stats'][state] += value

    def isCheckPoint(self) -> bool:
        return self._pointStats < 0

    def build(self) -> dict:
        return self._jsonPlayer
