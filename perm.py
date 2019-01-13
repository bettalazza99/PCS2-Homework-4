import itertools
n=6
def Permutation(n):
    a = itertools.permutations(range(1, n + 1))
    b = list(a)
    print (len(b))
    for i in b:
        print (' '.join(str(j) for j in i))

Permutation(6)
