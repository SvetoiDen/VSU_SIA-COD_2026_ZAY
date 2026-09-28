from code_task import *
import time

sizes = [4096, 16384, 65536, 262144, 500000, 1000000, 5_000_000, 10_000_000]
sep_print = "# ==================================== #"


def test_swift(func, arr, d):
    # если первые d данные в конце массива - True
    N = len(arr)
    test_true = arr[:d]

    res = func(arr, d)
    return res[(N - d):] == test_true


def main_test_func(n, d):
    print(sep_print)
    print("Тест 1 - первый способ через замену")
    print(test_swift(swift_temp, list(range(n)), d))
    print("Тест 2 - второй способ через цикл в цикле")
    print(test_swift(swift_loop, list(range(n)), d))
    print("Тест 3 - третий способ через разрезы")
    print(test_swift(swift_swift, list(range(n)), d))
    print(sep_print)


def ns_test(func, d):
    tempList = {}
    for n in sizes:
        a = list(range(n))
        listmid = []
        for _ in range(10):
            t1 = time.perf_counter_ns()
            res = func(a, d)
            t2 = time.perf_counter_ns()
            listmid.append(t1 - t2)
        timemid = sorted(listmid)[5]
        tempList[f"{n}"] = f"{timemid}"
        print(f"n = {n:>12} | время = {timemid / 1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")
    return tempList


def main_test(sizes):
    jsonData = {}

    print(sep_print)
    print("# Тестирование и время сдвига масссива на d позиции #")
    print(sep_print)

    d = 3  # первый способ

    print(f"# Первый способ при {sizes} элементах массива d={d} #")

    t1 = ns_test(swift_temp, d)
    jsonData['first_swift'] = t1

    print(sep_print)

    d = 4  # второй способ

    print(f"# Второй способ при {sizes} элементах массива при d={d} #")

    t2 = ns_test(swift_loop, d)
    jsonData['two_swift'] = t2

    print(sep_print)

    d = 12  # третий способ

    print(f"# Третий способ при {sizes} элементах массива при d={d} #")

    t3 = ns_test(swift_swift, d)
    jsonData['three_swift'] = t3

    print(sep_print)
    return jsonData


# def warmup():
#     try:
#         n = list(range(200))
#         for _ in range(500):
#             swift_loop(n, 12)
#             swift_temp(n, 3)
#             swift_swift(n, 4)
#     except Exception as e:
#         return "Прогрев не пройден. Ошибка в Python"
#
#     return "Прогрев пройден"


def csvRead(jsonData):
    import csv
    with open("csv_result.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(['Способ первый'])
        writer.writerow(['Размер', "время в ns"])
        for key, value in jsonData["first_swift"].items():
            writer.writerow([key.strip(), value.strip()])
        writer.writerow(['Способ второй'])
        writer.writerow(['Размер', "время в ns"])
        for key, value in jsonData["two_swift"].items():
            writer.writerow([key.strip(), value.strip()])
        writer.writerow(['Способ третий'])
        writer.writerow(['Размер', "время в ns"])
        for key, value in jsonData["three_swift"].items():
            writer.writerow([key.strip(), value.strip()])


if __name__ == "__main__":
    main_test_func(100, 6)
    js = main_test(sizes)
    csvRead(js)
