def multiply(m, n):
    if n > m:
        m, n = n, m

    if n == 0:
        return 0
    return m + multiply(m, n - 1)


# print(multiply(3, 5))


def rec(x, y):  # x ^ y
    if y > 0:
        return x * rec(x, y - 1)
    return 1


# print(rec(3, 5))


def hailstone(n):
    # n is even: n = n / 2
    # n is odd: n = n * 3 + 1
    # n == 1, stop
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n // 2)
    return 1 + hailstone(n * 3 + 1)


# print(hailstone(10))
# hailstone(10):
#     hailstone(5):
#         hailstone(16):
#             hailstone(8):
#                 hailstone(4):
#                     hailstone(2):
#                         hailstone(1):
#                         hailstone(1) -> 1
#                     hailstone(2) -> 2
#                 hailstone(4) -> 3
#             hailstone(8) -> 4
#         hailstone(16) -> 5
#     hailstone(5) -> 6
# hailstone(10) -> 7
# 7


def first_digit(n):
    return int(str(n)[:1])


def remaining_digit(n):
    if n < 10:
        return 0
    return int(str(n)[1:])


def merge(n1, n2):
    if n1 == 0 and n2 == 0:
        return ""
    first_digit_n1 = first_digit(n1)
    first_digit_n2 = first_digit(n2)
    if first_digit_n1 > first_digit_n2:
        return int(str(first_digit_n1) + str(merge(remaining_digit(n1), n2)))
    else:
        return int(str(first_digit_n2) + str(merge(n1, remaining_digit(n2))))


# print(merge(31, 42))  # 4321
# print(merge(21, 0))  # 21
# print(merge(21, 31))  # 3211
# print(merge(310, 420))  # 4321
# print(merge(310000, 420))  # 4321
# print(merge(22, 22))  # 2222


def make_func_repeater(f, x):
    def repeat(times):
        if times <= 1:
            return f(x)
        return f(repeat(times - 1))

    return repeat


# incr_1 = make_func_repeater(lambda x: x + 1, 1)
# print(incr_1(2))  # 3
# print(incr_1(5))  # 6


def is_prime(n):
    def prime_helper(cur):
        if n == 1:
            return False
        if cur == n:
            return True
        if n % cur == 0:
            return False
        return prime_helper(cur + 1)

    return prime_helper(2)


print(is_prime(7))  # True
print(is_prime(10))  # False
print(is_prime(1))  # False
