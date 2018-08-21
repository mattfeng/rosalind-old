#!/usr/bin/env python

def fib(n, k):
    # 1, 1, .., gets the nth term
    seq = [1, 1]
    for i in range(0, n - 2):
        seq.append(seq[-1] + k * seq[-2])

    return seq[n - 1]

n, k = (int(i) for i in open("rosalind_fib.txt").read().strip().split(" "))
print fib(n, k)
