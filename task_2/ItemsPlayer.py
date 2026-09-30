from enum import Enum


class ItemsPlayer(Enum):
    # ====================================== #

    ADVENTURE = []
    WARLOR = []
    MAG = []
    ENGINNER = []

    # ====================================== #

    def __init__(self, l):
        self._items = l
        self._N = len(l)

    def getItemIndex(self, index: int) -> str | None:
        if self._items[index] is None:
            return self._items[index]
        else:
            return None

    def getItemFirst(self) -> str:
        return self._items[0]

    def getItemEnd(self) -> str:
        return self._items[self._N - 1]
