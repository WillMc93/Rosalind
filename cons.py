import numpy as np
from itertools import product
from fasta_tools import fasta_read

file = './datasets/rosalind_cons.txt'

data = fasta_read(file)

# build matrix
matrix = np.zeros((4, 1), dtype=int)

decode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for _, seq in data.items():
	if len(seq) > matrix.shape[1]:
		old_matrix = matrix
		matrix = np.zeros((4, len(seq)), dtype=int)
		np.copyto(matrix, old_matrix)

	for idx, bp in enumerate(seq):
		matrix[decode[bp], idx] += 1
		
# build consensus
consensus = ''

# reverse decode dictionary
r_decode = dict()
for name, seq in decode.items():
	r_decode[seq] = name

# find the consensus
for y in range(matrix.shape[1]):
	con_char = ''
	max_count = 0

	for x in range(4):
		if matrix[x,y] > max_count:
			max_count = matrix[x,y]
			con_char = r_decode[x]

	consensus += con_char

# build matrix string
matrix_string = ''
for x in range(4):
	matrix_string += r_decode[x] + ': '
	
	for count in matrix[x]:
		matrix_string += str(count) + ' '

	matrix_string += '\n'

print(consensus)
print(matrix_string)