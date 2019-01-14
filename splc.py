f = open('C:\\Users\\Elisabetta\\Desktop\\rosalind_splc.txt','r')
sequences= [[block.split("\n",1)[0] , block.split("\n",1)[1].replace("\n","")] for block in f.read().split(">")[1:] ]
codRegion=sequences[0][1]
rna_bases= ['U', 'C', 'A', 'G']
codons = [a+b+c for a in rna_bases for b in rna_bases for c in rna_bases]
aminoacids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
dna_to_protein = dict(zip(codons, aminoacids))

def Protein(rnaseq):
   template = ""
   for i in range(0,len(rnaseq),3):
      template= template + dna_to_protein.get(rnaseq[i]+rnaseq[i+1]+rnaseq[i+2],"X")
   return template.strip("*")

for i in range(1,len(sequences)):
    codRegion = codRegion.replace(sequences[i][1],"")
codRegion = codRegion.replace("T","U")
print (Protein(codRegion))





