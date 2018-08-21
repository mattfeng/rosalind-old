#!/usr/bin/env python

def find_all_subs(main, pattern):
    p_len = len(pattern)
    locs = []
    for i in range(0, len(main) - p_len + 1):
        if main[i:i + p_len] == pattern:
            locs.append(i + 1)

    return locs


with open("rosalind_subs.txt") as f:
    main = f.readline().strip()
    pattern = f.readline().strip()

locs = find_all_subs(main, pattern)
for loc in locs:
    print loc,
