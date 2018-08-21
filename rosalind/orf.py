from .rna import transcribe
from .protein import translate
from .dna import reverse_complement
import re

def find_orfs(rna):
    found = map(lambda x: x[0], re.findall('(?=(AUG((A|C|G|U){3})*?(UAG|UGA|UAA)))', rna))
    return found