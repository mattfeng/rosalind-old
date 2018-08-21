#!/usr/bin/env python

def num_possibilities(protein):

    combos = {"F": 2, "L": 6, "S": 6, "Y": 2,
              "Q": 2, "K": 2, "G": 4, "W": 1,
              "H": 2, "P": 4, "I": 3, "M": 1,
              "T": 4, "N": 2, "E": 2, "C": 2,
              "R": 6, "V": 4, "A": 4, "D": 2}

    n_possible = 3
    for c in protein:
        n_possible *= combos[c]
        n_possible %= 1000000

    return n_possible

prot_str = open("rosalind_mrna.txt").read().strip()
print num_possibilities(prot_str)
