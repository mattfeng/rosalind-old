#!/usr/bin/env python

def prob_dominant(k, m, n):
    # k = # homozygous dominant
    # m = # heterozygous
    # n = # homozygous recessive

    # (a)  homozygous dominant + anything = dominant
    # (b1) homozygous recessive + heterozygous = 1/2 chance
    # (b2) homozygous recessive + homozygous dominant = dominant
    # (c1)  heterozygous + homozygous dominant = dominant
    # (c2)  heterozygous + heterozygous = 3/4
    # (c3)  heterozygous + homozygous recessive = 1/2 chance

    t = float(k + m + n)
    prob = 0
    prob += (k / t)
    prob += (n / t) * (m / (t -  1)) * (0.5)
    prob += (n / t) * (k / (t - 1))
    prob += (m / t) * (k / (t - 1))
    prob += (m / t) * ((m - 1) / (t - 1)) * (0.75)
    prob += (m / t) * (n / (t - 1)) * (0.5)

    return prob

k, m, n = (int(i) for i in open("rosalind_iprb.txt").read().strip().split(" "))
print prob_dominant(k, m, n)
