import sys
sys.path.insert(0, "/Users/mattfeng/bioinformatics")

from rosalind import fasta
import pandas as pd

data = fasta.read_fasta_to_dataframe("./rosalind_cons3.txt")

def consensus(df):
    return "".join(df.agg("mode", axis=1)[0])

class ProfileMatrix():

    def __init__(self, df):
        '''Creates a ProfileMatrix object from a DataFrame of FASTA strings.'''
        self.dataframe = df
        self.counts = self.dataframe.apply(pd.Series.value_counts, axis=1).fillna(0)
    
    def __repr__(self):
        ret = ""
        for base in "ACGT":
            counts = list(self.counts[base])
            ret += "{}: {}\n".format(base," ".join(map(lambda x: str(int(x)), counts)))
        return ret

profile = ProfileMatrix(data)
print(consensus(data))
print(profile)