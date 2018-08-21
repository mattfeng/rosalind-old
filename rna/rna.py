#!/usr/bin/env python

def transcribe(dna):
    return dna.replace("T", "U")

data = open("rosalind_rna.txt").read().strip()
print transcribe(data)
