import imp
from tree import Tree
from link import Link


def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[y]]

    elif x > y:
        return []

    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + i for i in a + b]


def merge(s1, s2):
    """Merges two sorted lists"""
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


def mergesort(seq):
    if len(seq) == 1:
        return seq
    else:
        return merge(mergesort(seq[: len(seq) // 2]), mergesort(seq[len(seq) // 2 :]))


print(mergesort([1, 4, 6, 2, 3, 9]))


def long_paths(tree, n):
    paths = []
    if n <= 0 and tree.is_leaf():
        paths.append(Link(tree.label))
    for b in tree.branches:
        for path in long_paths(b, n - 1):
            paths.append(Link(tree.label, path))
    return paths


t = Tree(3, [Tree(4), Tree(4), Tree(5)])
left = Tree(1, [Tree(2), t])
mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
whole = Tree(0, [left, Tree(13), mid, right])
for path in long_paths(whole, 2):
    print(path)

for path in long_paths(whole, 3):
    print(path)


def widest_level(t):
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)


def bake(banana, bread):
    banana.append(bread.append(1))
    bread += banana[: (len(banana) - 1)]
    banana.append(bread[bread[1]])
    return banana, bread


s = [1]
banana, bread = bake(s, [7, 2, s])


def amon(g):
    n = 0

    def u(s):
        nonlocal n
        f = lambda x: x + g.pop() + n
        n += 1
        return f(s)

    return u


g = [1, 2, 3]
skeld = amon(g)
pink = skeld(1)
purple = skeld(2)
