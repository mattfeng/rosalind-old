
def nprob(gen1, gen2):
    # genX = genotype
    probs = {}
    for allele1 in gen1:
        for allele2 in gen2:
            try:
                probs[allele1 + allele2] += 1. / 4.
            except:
                probs[allele1 + allele2] = 1. / 4.
    return probs

def predict_AaBb(K, N):
    # K = number of generations
    # N = lower bound of AaBb count
    for i in xrange(1000000):
        for gen in xrange(K):
