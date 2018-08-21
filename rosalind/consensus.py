from . import fasta
import pandas as pd

class ProfileMatrix(object):

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

def consensus(df):
    return "".join(df.agg("mode", axis=1)[0])