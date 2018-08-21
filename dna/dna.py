#!/usr/bin/env python

def pattern_count(text, pattern):
    cnt = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
            # # don't allow for overlapping patterns
            # i += len(pattern)
    return cnt

data = open("rosalind_dna.txt").read().strip()

print pattern_count(data, "A"),
print pattern_count(data, "C"),
print pattern_count(data, "G"),
print pattern_count(data, "T")
