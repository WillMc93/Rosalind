from Bio import SeqIO
import pycurl
import io

UNIPROT_URL = lambda ID: f'https://www.uniprot.org/uniprot/{ID}.fasta'

# read sequence data from File Object
def fasta_parse(file_obj):
	outp = dict()

	sequences = SeqIO.parse(file_obj, 'fasta')

	for seq in sequences:
		outp[seq.id]  = str(seq.seq)

	return outp

# read sequence data from file at file_path
def fasta_read(file_path):
	outp = dict()

	with open(file) as inp:
		outp = fasta_parse(inp)

	return outp

# wrap sequence data in file and read with fasta_parse
# for use in conjunction with pulling data from the internet
def fasta_read_raw(fasta):
	file = io.StringIO(fasta)
	
	return fasta_parse(file)

# gather fasta data from uniprot
def get_uniprot_fasta(ID):
	url = UNIPROT_URL(ID)

	data = 