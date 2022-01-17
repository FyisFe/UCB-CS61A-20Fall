from link import Link
from tree import Tree
from operator import mul


def sum_nums(link):
    """Write a function that takes in a a linked list and returns the sum of all its elements.
    You may assume all elements in lnk are integers."""
    if link.rest is Link.empty:
        return link.first

    return link.first + sum_nums(link.rest)


a = Link(1, Link(6, Link(7)))
print(sum_nums(a))


def multiply_lnks(lst_of_links):
    """Write a function that takes in a Python list of linked lists and multiplies them
    element-wise. It should return a new linked list.
    If not all of the Link objects are of equal length, return a linked list whose length is
    that of the shortest linked list given. You may assume the Link objects are shallow
    linked lists, and that lst of lnks contains at least one linked list."""
    val = 1
    new_list = []
    for links in lst_of_links:
        if links is Link.empty:
            return Link.empty
        val *= links.first
        new_list.append(links.rest)
    return Link(val, multiply_lnks(new_list))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(repr(p))


def flip_two(link):
    """Write a recursive function flip two that takes as input a linked list lnk
    and mutates lnk so that every pair is flipped."""
    cur = link
    while cur.rest is not Link.empty and cur is not Link.empty:
        cur.first, cur.rest.first = cur.rest.first, cur.first
        cur = cur.rest.rest


one_link = Link(1)
flip_two(one_link)
print(repr(one_link))
lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
flip_two(lnk)
print(repr(lnk))


def filter_link(link, f):
    """Implement filter link, which takes in a linked list link and a function
    f and returns a generator which yields the values of link for which f returns True.
    Try to implement this both using a while loop and without using any form of
    iteration."""
    if link is Link.empty:
        return

    if f(link.first):
        yield link.first

    yield from filter_link(link.rest, f)

    #  while loop version:
    #  while link is not Link.empty:
    #     if f(link.first):
    #         yield link.first
    #     link = link.rest


link = Link(1, Link(2, Link(3)))
g = filter_link(link, lambda x: x % 2 == 0)
print(list(g))
print(list(filter_link(link, lambda x: x % 2 != 0)))


def make_even(t):
    """Define a function make even which takes in a tree t whose values are integers, and
    mutates the tree such that all the odd integers are increased by 1 and all the even
    integers remain the same."""

    if t.label % 2 != 0:
        t.label = t.label + 1

    if Tree.is_leaf(t):
        return

    for b in t.branches:
        make_even(b)


t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
make_even(t)
print("make_even: ")
Tree.print_tree(t)
# 2
#   2
#     4
#   4
#   6


def square_tree(t):
    """Define a function square tree(t) that squares every value in the non-empty tree
    t. You can assume that every value is a number."""

    t.label = t.label ** 2

    if Tree.is_leaf(t):
        return

    for b in t.branches:
        square_tree(b)


t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
square_tree(t)
print("square_tree: ")
Tree.print_tree(t)
# 1
#   4
#     9
#   16
#   25


def find_paths(t, entry):
    """Define the procedure find paths that, given a Tree t and an entry,
    returns a list of lists containing the nodes along each path from the root of t to
    entry. You may return the paths in any order."""
    lst = []

    def helper(t, entry, cur_lst=[]):
        cur_lst.append(t.label)

        if t.label == entry:
            lst.append(cur_lst)

        if Tree.is_leaf(t):
            return

        for b in t.branches:
            new_lst = cur_lst[:]
            helper(b, entry, new_lst)

    helper(t, entry)
    return lst


tree_ex = Tree(
    2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])]
)
print(find_paths(tree_ex, 5))  # [[2, 7, 6, 5], [2, 1, 5]]


def combine_tree(t1, t2, combiner):
    """Write a function that combines the values of two trees t1 and t2 together with the
    combiner function. Assume that t1 and t2 have identical structure. This function
    should return a new tree.

    Hint: consider using the zip() function, which returns an iterator of tuples where
    the first items of each iterable object passed in form the first tuple, the second items
    are paired together and form the second tuple, and so on and so forth."""
    if Tree.is_leaf(t1):
        return Tree(combiner(t1.label, t2.label))

    return Tree(
        combiner(t1.label, t2.label),
        [combine_tree(b[0], b[1], combiner) for b in zip(t1.branches, t2.branches)],
    )


a = Tree(1, [Tree(2, [Tree(3)])])
b = Tree(4, [Tree(5, [Tree(6)])])
print("combine_tree: ")
Tree.print_tree(combine_tree(a, b, mul))
# 4
#   10
#     18


def alt_tree_map(t, map_fn):
    """Implement the alt tree map function that, given a function and a Tree, applies the
    function to all of the data at every other level of the tree, starting at the root."""

    def helper(t, map_fn, level=0):
        if level % 2 == 0:
            t.label = map_fn(t.label)

        for b in t.branches:
            helper(b, map_fn, level + 1)

    helper(t, map_fn)


t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
alt_tree_map(t, lambda x: -x)
print("alt_tree_map: ")
Tree.print_tree(t)
# -1
#   2
#     -3
#   4
