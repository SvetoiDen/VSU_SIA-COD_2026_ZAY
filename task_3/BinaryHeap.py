from typing import Iterable, List, Optional


class BinaryHeap:
    def __init__(
            self,
            items: Optional[Iterable[int]] = None,
            *,
            max_heap: bool = True,
    ) -> None:
        self._heap: List[int] = []
        self._max_heap: bool = max_heap
        if items is not None:
            self._heap = list(items)
            self._build_heap()

    # ---------- внутреннее ----------

    def _sift_up(self, i: int) -> None:
        heap = self._heap
        if self._max_heap:
            while i > 0:
                parent = (i - 1) >> 1
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
        else:
            while i > 0:
                parent = (i - 1) >> 1
                if heap[i] < heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break

    def _sift_down(self, i: int) -> None:
        heap = self._heap
        n = len(heap)
        if self._max_heap:
            while True:
                left = 2 * i + 1
                if left >= n:
                    return
                right = left + 1
                best = left
                if right < n and heap[right] > heap[left]:
                    best = right
                if heap[best] > heap[i]:
                    heap[i], heap[best] = heap[best], heap[i]
                    i = best
                else:
                    return
        else:
            while True:
                left = 2 * i + 1
                if left >= n:
                    return
                right = left + 1
                best = left
                if right < n and heap[right] < heap[left]:
                    best = right
                if heap[best] < heap[i]:
                    heap[i], heap[best] = heap[best], heap[i]
                    i = best
                else:
                    return

    def _build_heap(self) -> None:
        # O(n): просеиваем вниз только внутренние узлы
        for i in range(self.size() // 2 - 1, -1, -1):
            self._sift_down(i)

    # ---------- публичный API ----------

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return not self._heap

    def peek(self) -> int:
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def push(self, value: int) -> None:
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def pop(self) -> int:
        heap = self._heap
        if not heap:
            raise IndexError("pop from empty heap")
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            self._sift_down(0)
        return top

    def replace_top(self, value: int) -> int:
        """Заменить корень на value, вернуть старый корень. O(log n)."""
        heap = self._heap
        if not heap:
            raise IndexError("replace_top from empty heap")
        old = heap[0]
        heap[0] = value
        self._sift_down(0)
        return old

    def heapify(self, items: Optional[Iterable[int]] = None) -> None:
        """Построить кучу по месту за O(n)."""
        if items is not None:
            self._heap = list(items)
        self._build_heap()

    def __repr__(self) -> str:
        return (
            f"BinaryHeap(size={len(self._heap)}, "
            f"max_heap={self._max_heap}, data={self._heap!r})"
        )
