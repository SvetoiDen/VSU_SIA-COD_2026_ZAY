from typing import Any


class Player():
    def __init__(self) -> None:
        self.jsonPlayer = {}

    def add(self, key: str, value: Any) -> None:
        self.jsonPlayer[key] = value

    def result(self) -> None:
        pass
