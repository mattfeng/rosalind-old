#!/usr/bin/env python

def expected_dominant(couples):
    # AA-AA
    # AA-Aa
    # AA-aa
    # Aa-Aa
    # Aa-aa
    # aa-aa
    return sum(couples[0:3]) * 2 + couples[3] * 1.5 + couples[4]

couples = [int(i) for i in open("rosalind_iev.txt").read().split(" ")]
print expected_dominant(couples)
