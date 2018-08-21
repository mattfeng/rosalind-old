#!/usr/bin/env python

def hamming(a, b):
    diff = 0
    for i, j in zip(a, b):
        if i != j:
            diff += 1

    return diff

with open("rosalind_hamm.txt") as f:
    a = f.readline().strip()
    b = f.readline().strip()

print hamming(a, b)
