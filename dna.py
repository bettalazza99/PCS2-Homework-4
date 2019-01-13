a = open('C:\\Users\\Elisabetta\\Desktop\\rosalind_dna.txt', 'r')
mylist = a.read()
print(mylist.count('A'), mylist.count('C'), mylist.count('G'), mylist.count('T'))
