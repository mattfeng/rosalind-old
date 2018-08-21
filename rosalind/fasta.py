import pandas as pd

def read_fasta_to_dataframe(filename):
    data = pd.DataFrame()
    with open(filename) as f:
        header = f.next().strip()

        while True:
            agg = "" # aggregates the DNA string
            try:
                line = f.next()
                while not line.startswith(">"): # while not a header, add to the agg
                    agg += line.strip()
                    line = f.next()
                data[header] = pd.Series(list(agg)) # we found a new header, so save the value of previous
                header = line.strip()
                agg = ""
            except StopIteration:
                data[header] = pd.Series(list(agg))
                print("[i] Finished reading file: {}".format(filename))
                break
    
    return data
