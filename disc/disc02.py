def keep_ints(cond, n):
    for i in range(1, n + 1):
        if cond(i):
            print(i)


def is_even(x):
    return x % 2 == 0


keep_ints(is_even, 5)


def make_deeper(n):
    def keep_ints(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)

    return keep_ints


make_deeper(5)(is_even)
