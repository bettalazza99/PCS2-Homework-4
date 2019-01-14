codontable = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }

def cmpl_rvrs(sequence):
    reverse = sequence[::-1]
    reverse = ''
    for e in reverse:
        if e == "A":
            reverse += "T"
        if e == "T":
            reverse += "A"
        if e == "C":
            reverse += "G"
        if e == "G":
            reverse += "C"
    return reverse

def find_str_codon(sequence):
    codstrs= []
    for i in range(len(sequence)-3):
        if sequence[i:i+3] == 'ATG':
            new_seq = sequence[i:]
            k = 0
            codstr = ""
            while k < len(new_seq)-3:
                if new_seq[k:k+3] in ("TAA", "TAG", "TGA"):
                    codstr = new_seq[:k]
                    codstrs.append(codstr)
                    break
                else:
                    k += 3
    return codstrs

def trans(coding_string):
    i = 0
    AAsequence = ""
    while i <= len(coding_string) - 3:
        AAsequence += codontable[coding_string[i:i+3]]
        i = i + 3
    if AAsequence:
        return AAsequence

with open("C:\\Users\\Elisabetta\\Desktop\\rosalind_orf.txt", "r") as f:
    lines = f.readlines()
    seq = ''
    for i in lines:
        if i[0]!= ">":
            line = i.strip()
            seq += line
    seqs = [seq, cmpl_rvrs(seq)]
    all_cod_seq = []

    for seq in seqs:
        codstrs = find_str_codon(seq)
        all_cod_seq += codstrs
    trans_seq = [all_cod_seq[0]]

    for seq in all_cod_seq:
        if seq not in trans_seq:
            trans_seq += [seq]

    for seq in trans_seq:
        print (trans(seq))


