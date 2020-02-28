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

def check_for_motif(ID, motif=motif):

	# make motif into regex and compile
	motif = regexify(motif)

	pattern = re.compile(motif)

	# read data from uniprot and format
	data = get_uniprot_fasta(ID)
	data = fasta_read_raw(data)

	assert(len(data.items()) == 1)

	_, data = list(data.items())[0]

	# find all matches for the motif
	results = []
	pos = 0
	while True:
		result = pattern.search(data, pos)

		if result is None:
			break
		results.append(result.start()+1)
		pos = result.start() + 1

	return results

if __name__ == '__main__':

	with open(file) as f:
		for ID in f:
			ID = ID.strip()
		
			results = check_for_motif(ID)

			outp = ''
			if len(results) > 0:
				print(ID)
				outp = ""
				for result in results:
					outp += str(result) + " "

				print(outp)

