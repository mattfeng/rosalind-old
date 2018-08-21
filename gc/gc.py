#!/usr/bin/env python

def gc(fasta):
    fasta_lines = fasta.split("\n")
    header = fasta_lines[0].strip()

    gc_count = 0
    total_count = 0
    for line in fasta_lines[1:]:
        line = line.strip()
        print line
        gc_count += line.count("G")
        gc_count += line.count("C")
        total_count += len(line)

    return header, float(gc_count) / float(total_count) * 100.0


with open("rosalind_gc.txt") as f:
    fasta_strings = []
    fasta = f.readline()
    for line in f:
        if line.startswith(">"):
            fasta_strings.append(fasta)
            fasta = ""
        fasta += line
    fasta_strings.append(fasta)

gc_content = []
for fasta in fasta_strings:
    gc_content.append(gc(fasta))

for content in gc_content:
    print content

max_gc_content = max(gc_content, key=lambda x: x[1])
print max_gc_content[0][1:]
print round(max_gc_content[1], 6)
