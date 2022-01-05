def count_stair_ways(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    result = 0
    for i in range(1, k + 1):
        result += count_k(n - i, k)
    return result


# print(count_k(3, 3))  # 4
# print(count_k(4, 4))  # 8
# print(count_k(10, 3))  # 274
# print(count_k(300, 1))  # 1

list_comprehension = [x * x - 3 for x in [1, 2, 3, 4, 5] if x % 2 == 1]  # [-2, 6, 22]
# filter => [1, 3, 5] => calculating

a = [1, 5, 4, [2, 3], 3]

# a[0] == 1 a[-1] == 3
# len(a) == 5
# 2 in a == False
# 4 in a == True
# a[3][0] = 2


def even_weighted(s):
    list = []
    for i in range(len(s)):
        if i % 2 == 0:
            list.append(s[i] * i)

    return list


# print(even_weighted([1, 2, 3, 4, 5, 6]))  # [0, 6, 20]


def max_product(s):
    if not len(s):
        return 1
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))


print(max_product([10, 3, 1, 9, 2]))  # 90
print(max_product([5, 10, 5, 10, 5]))  # 125
print(max_product([]))  # 1
