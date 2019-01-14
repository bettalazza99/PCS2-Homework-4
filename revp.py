def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([complements[a] for a in reversed(s)])

with open("C:\\Users\\Elisabetta\\Desktop\\rosalind_revp.txt")as dna:
    dna_str = dna.readlines()
    seq = ""
    for line in dna_str:
        line = line.strip()
        if line[0] != ">":
            seq += line
    for i in range(len(seq)):
        for n in range(4,13):
            if seq[i:i+n] == reverse_complement(seq[i:i+n]):
                if i + n <= len(seq):
                    print (i+1, n)

