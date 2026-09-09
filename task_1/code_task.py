# Первый способ

def swift_temp(arr, d):
    pass


# ============================ #
# Второй способ

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
