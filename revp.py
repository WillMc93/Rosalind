from fasta_tools import fasta_read, just_seq

def reverse_compliment(seq):
	compliments = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

	seq = seq[::-1]
	rc = ''
	for i in range(len(seq)):
		rc += compliments[seq[i]]

	return rc


