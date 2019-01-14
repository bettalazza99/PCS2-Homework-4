with open('C:\\Users\\Elisabetta\\Desktop\\rosalind_pdst.txt','r') as f:
    read_data = f.read().split('>')[1:]
s = [i.replace('\n', '')[13:] for i in read_data]
seq = [x for x in s]

length = len(s[0])
matrix = [[] for i in range(len(s))]

for i in range(len(s)):
    for j in range(i, len(s)):
        hamming_distance = sum(a != b for a, b in zip(seq[i], seq[j])) / length
        matrix[i].append(hamming_distance)
        if i != j:
            matrix[j].append(hamming_distance)

print('\n'.join(' '.join('%.5f' % i for i in row) for row in matrix))
