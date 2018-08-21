#!/usr/bin/env python

def fibd(n, m):
    n_adults = [0 for _ in range(m - 1)]
    n_child = 1

    for _ in range(n - 1):
        n_child_tmp = sum(n_adults)
        n_adults.pop()
        n_adults.insert(0, n_child)
        n_child = n_child_tmp

    return sum(n_adults) + n_child


n, m = (int(i) for i in open("rosalind_fibd.txt").read().strip().split(" "))
print fibd(n, m)
