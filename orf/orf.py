import sys
sys.path.insert(0, "/Users/mattfeng/bioinformatics")

from rosalind.fasta import read_fasta_to_dataframe
from rosalind.rna import transcribe
from rosalind.protein import translate
from rosalind.dna import reverse_complement

import re

def find_orfs(rna):
    found = map(lambda x: x[0], re.findall('(?=(AUG((A|C|G|U){3})*?(UAG|UGA|UAA)))', rna))
    return found

data = read_fasta_to_dataframe("./rosalind_orf.txt")
dna = "".join(data.ix[:, 0])

dna_rev = reverse_complement(dna)
rna = transcribe(dna)
rna_rev = transcribe(dna_rev)

orfs = []
orfs.extend(find_orfs(rna))
orfs.extend(find_orfs(rna_rev))

proteins = set(map(translate, orfs))
for prot in proteins:
    print(prot)
