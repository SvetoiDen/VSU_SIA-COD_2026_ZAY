from code_task import *
import time

sizes = [4, 32, 128, 512, 1024, 4096, 16384, 65536, 262144]


def main_test(sizes):
    jsonData = {}

    sep_print = "# ==================================== #"
    print(sep_print)
    print("# Тестирование и время сдвига масссива на d позиции #")
    print(sep_print)
    d = 3 # первый способ
    print(f"# Первый способ при {sizes} элементах массива d={d} #")

    tempList = {}
    for n in sizes:
        a = list(range(n))
        t1 = time.perf_counter_ns()
        res = swift_temp(a, d)
        t2 = time.perf_counter_ns()
        tempList[f"{n}"] = f"{(t2 - t1)}"
        print(f"n = {n:>6} | время = {(t2 - t1) / 1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")
    jsonData['first_swift'] = tempList

    print(sep_print)
    d = 4 # второй способ
    print(f"# Второй способ при {sizes} элементах массива при d={d} #")

    tempList = {}
    for n in sizes:
        a = list(range(n))
        t1 = time.perf_counter_ns()
        res = swift_loop(a, d)
        t2 = time.perf_counter_ns()
        tempList[f"{n}"] = f"{(t2 - t1)}"
        print(f"n = {n:>6} | время = {(t2 - t1) / 1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")
    jsonData['two_swift'] = tempList

    print(sep_print)
    d = 12 # третий способ
    print(f"# Третий способ при {sizes} элементах массива при d={d} #")

    tempList = {}
    for n in sizes:
        a = list(range(n))
        t1 = time.perf_counter_ns()
        res = swift_swift(a, d)
        t2 = time.perf_counter_ns()
        tempList[f"{n}"] = f"{(t2 - t1)}"
        print(f"n = {n:>6} | время = {(t2 - t1) / 1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")
    jsonData['three_swift'] = tempList

    print(sep_print)
    return jsonData


def warmup():
    try:
        n = list(range(200))
        for _ in range(500):
            swift_loop(n, 12)
            swift_temp(n, 3)
            swift_swift(n, 4)
    except Exception as e:
        return "Прогрев не пройден. Ошибка в Python"

    return "Прогрев пройден"


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
    print(warmup())
    js = main_test(sizes)
    csvRead(js)
