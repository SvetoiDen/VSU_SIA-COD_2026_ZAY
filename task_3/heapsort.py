from binaryheap import Comparator


def heapsort_inplace(arr: list, cmp: Comparator, counter: list) -> None:
    """
    Сортирует arr на месте по возрастанию.
    cmp(a, b) должна возвращать True, если a > b (max-куча).
    counter[0] увеличивается на каждом сравнении.
    """
    n = len(arr)

    def sift_down(i: int, n: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i
            if left < n:
                counter[0] += 1
                if cmp(arr[left], arr[best]):
                    best = left
            if right < n:
                counter[0] += 1
                if cmp(arr[right], arr[best]):
                    best = right
            if best == i:
                break
            arr[i], arr[best] = arr[best], arr[i]
            i = best

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    # Извлечение элементов
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end)
