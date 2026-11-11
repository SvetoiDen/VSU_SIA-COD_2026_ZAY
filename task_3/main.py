from typing import Iterable, List

from TopFilmCost import TopFilmCost, Request


def top_k(requests: Iterable[Request], k: int) -> List[str]:
    tk = TopFilmCost(k)
    for arrival, (rid, cost) in enumerate(requests):
        tk.add(rid, cost, arrival)
    return tk.result()


def run_tests() -> None:
    # k = 0
    assert top_k([("Фильм 1", 5), ("Фильм 2", 10)], 0) == []

    # k = 1
    reqs = [("a", 5), ("b", 10), ("c", 7), ("d", 10)]
    # b и d одинаковы по cost, но b поступила раньше
    assert top_k(reqs, 1) == ["b"]

    # k больше числа заявок
    reqs = [("a", 5), ("b", 10), ("c", 7)]
    assert top_k(reqs, 5) == ["b", "c", "a"]

    # равные стоимости: выигрывают более ранние
    reqs = [("a", 10), ("b", 10), ("c", 10), ("d", 10)]
    assert top_k(reqs, 3) == ["a", "b", "c"]

    # смешанный случай
    reqs = [("a", 10), ("b", 9), ("c", 10), ("d", 8), ("e", 9)]
    # cost=10: a, c; затем cost=9: b (раньше e)
    assert top_k(reqs, 3) == ["a", "c", "b"]

    # отрицательные стоимости
    reqs = [("a", -5), ("b", -1), ("c", -3)]
    assert top_k(reqs, 2) == ["b", "c"]

    print("all tests passed")


if __name__ == "__main__":
    run_tests()
