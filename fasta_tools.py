from Bio import SeqIO

def fasta_read(file):
	outp = dict()

	sequences = ''

	with open(file) as inp:
		sequences = SeqIO.parse(inp, 'fasta')

		for seq in sequences:
			outp[seq.id]  = str(seq.seq)

	return outp

