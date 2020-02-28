from fasta_tools import fasta_read
from rna_table import acid_lookup, codon_lookup

from itertools import product

import re

file = './datasets/rosalind_orf.txt'

start_pat = re.compile(acid_lookup('M')[0])

stop_pats = acid_lookup('*')
for i in range(len(stops)): # it's three but good coding
	stop_pats[i] = re.compile(stops[i])

def get_orf(seq):

	starts = start.finditer(seq)

	for start, end in product(starts, stops):

		start = start.start()




if __name__ == '__main__':
	