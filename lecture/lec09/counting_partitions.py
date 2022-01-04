# The number of partitions of a positive integer n, using parts up to size m, is the number of ways in which n can be expressed as teh sum of positive integer parts up to m in increasing order.


# Two possibilities:
# 1. Use at least one m
# 2. Do not use any m


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)


print(count_partitions(6, 4))
