from typing import Any, Callable, List, Optional

Comparator = Callable[[Any, Any], bool]


class BinaryHeap:
    def __init__(self, items: Optional[List[Any]] = None, *, comparator: Optional[Comparator] = None):
        self._cmp = comparator if comparator is not None else (lambda a, b: a < b)
        if items is None:
            self._heap: List[Any] = []
        else:
            self._heap = list(items)
            self._heapify()

    def _heapify(self) -> None:
        n = len(self._heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i: int) -> None:
        heap = self._heap
        cmp = self._cmp
        while i > 0:
            parent = (i - 1) // 2
            if cmp(heap[i], heap[parent]):
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        heap = self._heap
        n = len(heap)
        cmp = self._cmp
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i
            if left < n and cmp(heap[left], heap[best]):
                best = left
            if right < n and cmp(heap[right], heap[best]):
                best = right
            if best == i:
                break
            heap[i], heap[best] = heap[best], heap[i]
            i = best

    def push(self, item: Any) -> None:
        self._heap.append(item)
        self._sift_up(len(self._heap) - 1)

    def pop(self) -> Any:
        if not self._heap:
            raise IndexError("pop from empty heap")
        heap = self._heap
        root = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            self._sift_down(0)
        return root

    def peek(self) -> Any:
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def replace_top(self, item: Any) -> Any:
        if not self._heap:
            raise IndexError("replace_top from empty heap")
        old = self._heap[0]
        self._heap[0] = item
        self._sift_down(0)
        return old

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)
