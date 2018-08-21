from string import maketrans

DNA_TO_RNA = maketrans("ACGT", "ACGU")

def transcribe(dna):
    return dna.translate(DNA_TO_RNA)
