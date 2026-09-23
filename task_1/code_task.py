# Первый способ
# Худший случай - 0(n)

def swift_temp(arr, d):
    N = len(arr)
    if d > N:
        d %= N
    temp = arr[:d]

    del arr[:d]
    arr += temp
    return arr


# ============================ #
# Второй способ
# Худший случай - 0(d(N-1))

def swift_loop(arr, d):
    N = len(arr)
    for _ in range(d):
        a = arr[0]
        for i in range(N - 1):
            arr[i] = arr[i + 1]
        arr[N - 1] = a
    return arr


# ============================ #
# Третий способ

def swift_swift(arr, d):
    N = len(arr)
    leftarr = arr[:d]
    rightarr = arr[d:]

    res = (leftarr[::-1] + rightarr[::-1])[::-1]
    return res
