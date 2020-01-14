from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

file = './datasets/rosalind_prot.txt'
data = ''

with open(file) as f:
	data = f.readline()
	data.strip()

data = Seq(data)

print(data.translate())