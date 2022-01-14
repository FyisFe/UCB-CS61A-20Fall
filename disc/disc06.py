def memory(n):
    def f(g):
        nonlocal n
        n = g(n)
        return n

    return f


f = memory(10)
print(f(lambda x: x * 2))  # 20
print(f(lambda x: x - 7))  # 13
print(f(lambda x: x > 5))  # True

s1 = [1, 2, 3]
s2 = s1
print(s1 is s2)  # True

s2.extend([5, 6])
print(s1[4])  # 6

s1.append([-1, 0, 1])
print(s2[5])  # [-1, 0, 1]

s3 = s2[:]
s3.insert(3, s2.pop(3))

print(len(s1))  # 5
# s1 is s2 = [1, 2, 3, 6, [-1, 0, 1]]

print(s1[4] is s3[6])  # True

print(s3[s2[4][1]])  # 1 S3[0]

print(s1[:3] is s2[:3])  # False
print(s1[:3] == s2[:3])  # True
