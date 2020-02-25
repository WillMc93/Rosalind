import re
from fasta_tools import fasta_read_raw, get_uniprot_fasta

file = './datasets/rosalind_mprt.txt'

motif = 'N{P}[ST]{P}'



def regexify(motif=motif):
	left_pttrn = r'{'
	left_repl = '[^'
	right_pttrn = r'}'
	right_repl = ']'

	motif = re.sub(left_pttrn, left_repl, motif) 
	motif = re.sub(right_pttrn, right_repl, motif)


	return motif
	
def get_fasta
