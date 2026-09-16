from code_task import *
import time

sizes = [8, 32, 128, 512, 1024, 4096, 16384, 65536, 262144]
sep_print = "# ==================================== #"
print(sep_print)
print("# Тестирование и время сдвига масссива на d позиции #")
print(sep_print)
print(f"# Первый способ при {sizes} элементах массива d=3 #")

d = 3

for n in sizes:
    a = list(range(n))
    t1 = time.perf_counter_ns()
    res = swift_temp(a, d)
    t2 = time.perf_counter_ns()
    print(f"n = {n:>6} | время = {(t2 - t1)/1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")

print(sep_print)
print(f"# Второй способ при {sizes} элементах массива при d=6 #")

d = 6

for n in sizes:
    a = list(range(n))
    t1 = time.perf_counter_ns()
    res = swift_loop(a, d)
    t2 = time.perf_counter_ns()
    print(f"n = {n:>6} | время = {(t2 - t1)/1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")

print(sep_print)
print(f"# Третий способ при {sizes} элементах массива при d=8 #")

d = 8

for n in sizes:
    a = list(range(n))
    t1 = time.perf_counter_ns()
    res = swift_swift(a, d)
    t2 = time.perf_counter_ns()
    print(f"n = {n:>6} | время = {(t2 - t1)/1_000_000:8.4f} ms | результат[:{d}+2] = {res[:(d + 2)]}")

print(sep_print)
