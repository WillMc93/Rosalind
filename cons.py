import numpy as np
from itertools import product
from fasta_tools import fasta_read

file = './datasets/rosalind_cons.txt'

data = fasta_read(file)

# build matrix
matrix = np.zeros((4, 1000), dtype=int)

decode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for _, seq in data.items():
	for idx, bp in enumerate(seq):
		matrix[decode[bp], idx] += 1
		
# build consensus
for x,y in product(range(4), range(1000)):
	