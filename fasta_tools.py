from Bio import SeqIO
import pycurl
import io

def fasta_parse(file_obj):
	outp = dict()

	sequences = SeqIO.parse(file_obj, 'fasta')

	for seq in sequences:
		outp[seq.id]  = str(seq.seq)

	return outp

def fasta_read(file):
	outp = dict()

	with open(file) as inp:
		outp = fasta_parse(inp)

	return outp

def fasta_read_raw(fasta):
	file = io.StringIO(fasta)

	
	return fasta_read(file)

def get_uniprot_fasta(ID):
	url = lambda ID: f'https://www.uniprot.org/uniprot/{ID}.fasta'