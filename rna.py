def TranscribeDNAtoRNA(dna):
    return dna.replace("T", "U")

if __name__ == '__main__':
    dna="GAGAGTAACCAGTGCACGTAATGTGGTGTGTGATGCTACCTTGCCTGGGGTTGGAGGAGCCCTGACGGATAGAGCCTCAATATGGAAAAGGCGGGGCGCACCCCACGCAGTTATCCCCTCAAGAGCACCCGGCGGCAGCCTAGGGAAGGGTCACTGCCAATTTCTGCGGTCCAGGCCGCCACGAGCGTATAGCCGTTCGCTTCTCAACACAAAGGGAAAACGTCCCCCTGTACTACACATCGTGAATGCTACCACTTTTAAGTAGGACCCGCGGTTAACTTGTGCGACCGGCTGTCTAGTTGTGAGGGCGGGCCATAGGTAAGGGTCAATCACCTGCGAAGGCTGGCCTATAAGCCACGAGAGGATCACTCATCAATCTAGTCCAATAATCCTAATTAGCCCATAGTTTCGGGTAGAACCCCATAAGGTGCGGCCATCAGAACTCGATAAATTAATCCATCACAGGCACGGCAATGGATCTGTGTAAATCATGTGAAAGCGAATGAGCTGCTTACAAAATATTGCTCAAACGTATTTCACGGTACCTAGGAGTCCTGTTGTGAACTTGGAGCGCGAACGCTTTGGTTATATGGCGTCTAGAGGCTATTTCGCGGTAAGTCCGTACGGGAGAGGATTCGGACCCGTAACGGGTCATAGAGCTTAGTAGTAGGCATTCGCCATAGGGAAATGCCTCCTTAGGGTAAGGAGCATTGATTCAAATCGCATTGACTGTAATATCCTGCTCTGATTCGACTCTTTTCAACGAGCCTAAGCGCTCACCAATAGGATGCCGTCGTAGGGTCCTTCTTGTGAGAGATACTGCAACAGCATGCTGCATGCAGCGACGCCCCTATGTACCCTGCTTGTCGTGCATGTATCCACCCCGTCAAAACACCCTTACTGATCATACTCTGACACCTCAACTTGGAGATGCAGCAGCCATTAGTTGCGCTATGCGGTGTTTGGGT"
    print(TranscribeDNAtoRNA(dna))
