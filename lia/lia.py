def product(l):
    return reduce(lambda a, b: a * b, l)

def choose(n, r):
    return product(range(n, n - r, -1)) / product(range(1, r + 1))
    
def predict_AaBb(gen_k, n):
    # Key insight:
    # No matter what genotype an organism is, when mating with a AaBb,
    # the probability that the offspring will be heterozygous AaBb
    # is ALWAYS 25%.

    n_children = 2 ** gen_k
    ans = 0
    for i in range(n, n_children + 1):
        ans += choose(n_children, i) * (0.25 ** i) * (0.75 ** (n_children - i))
    return ans

print(predict_AaBb(7, 31))
