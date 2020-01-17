from fasta_tools import fasta_read

import numpy as np

file = './datasets/rosalind_'

def lcsm(file):

	data = fasta_read(file)

	shortest = tuple('', float('inf'))
	for item in data.items():
		if len(item[1]) < len(shortest[1]):
			shortest = item
		



if __name__ == '__main__':
	