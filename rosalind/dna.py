from string import maketrans
REVERSE_COMPLEMENT = maketrans("ACGT", "TGCA")

def reverse_complement(dna):
    return dna.translate(REVERSE_COMPLEMENT)[::-1]