#!/usr/bin/env python

def complement(dna):
    pair = {"A":"T",
            "T":"A",
            "C":"G",
            "G":"C"}

    ret = ""
    for c in dna:
        ret += pair[c]

    return ret


def rev_complement(dna):
    return complement(dna)[::-1]

data = open("rosalind_revc.txt").read().strip()
print rev_complement(data)
