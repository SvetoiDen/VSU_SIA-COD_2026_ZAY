from BinaryHeap import BinaryHeap
from typing import Iterable, List, Tuple

Request = Tuple[str, int]


class TopFilmCost:
    def __init__(self, k: int) -> None:
        if k < 0:
            raise ValueError("k must be >= 0")
        self._k = k
        self._heap = BinaryHeap(max_heap=False)
        self._data: dict[int, tuple[int, int, str]] = {}
        self._bits = 1

    def _encode(self, cost: int, arrival: int) -> int:
        return (cost << self._bits) - arrival

    def _reencode(self) -> None:
        new_data: dict[int, tuple[int, int, str]] = {}
        new_keys: list[int] = []

        for _, (cost, arrival, rid) in self._data.items():
            key = self._encode(cost, arrival)
            new_keys.append(key)
            new_data[key] = (cost, arrival, rid)

        self._data = new_data
        self._heap = BinaryHeap(new_keys, max_heap=False)

    def _ensure_bits(self, arrival: int) -> None:
        need = max(1, arrival.bit_length())
        if need > self._bits:
            self._bits = need
            self._reencode()

    def add(self, rid: str, cost: int, arrival: int) -> None:
        if self._k == 0:
            return

        self._ensure_bits(arrival)
        key = self._encode(cost, arrival)

        if self._heap.size() < self._k:
            self._heap.push(key)
            self._data[key] = (cost, arrival, rid)
            return

        worst_key = self._heap.peek()

        # key > worst_key  <=> новая заявка лучше худшей выбранной
        if key > worst_key:
            old_key = self._heap.replace_top(key)
            del self._data[old_key]
            self._data[key] = (cost, arrival, rid)

    def result(self) -> List[str]:
        # сортировка разрешена только для выбранных, их <= k
        keys = sorted(self._data.keys(), reverse=True)
        return [self._data[key][2] for key in keys]
