from fasta_tools import fasta_read, just_seq
from codon_tables import acid_lookup

import re

file = './datasets/rosalind_orf.txt'

# translate into all three possible amino strings
def translate_seq(seq):
	amino_strings = []

	for offset in range(0, 3):
		translated = ''

		for i in range(offset, len(seq), 3):
			j = i + 3

			codon = seq[i:j]
			acid = acid_lookup(codon)

			translated += acid

		amino_strings.append(translated)
	# print(amino_strings)

	return amino_strings


def reverse_compliment(seq):
	compliments = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

	seq = seq[::-1]
	rc = ''
	for i in range(len(seq)):
		rc += compliments[seq[i]]

	return rc

def extract_orfs(amino_strings):
	start_p = re.compile(r'M')
	stop_p = re.compile(r'\*')

	orfs = []

	for seq in amino_strings:
		starts = start_p.finditer(seq)

		for start in starts:
			start = start.start()
			stop = stop_p.search(seq, pos=start)

			if stop:
				stop = stop.start()
				orf = seq[start:stop]

				orfs.append(orf)

	return orfs


if __name__ == '__main__':
	data = fasta_read(file)
	data = just_seq(data)

	for seq in data:
		rc_seq = reverse_compliment(seq)
		
		translated = translate_seq(seq)
		translated += translate_seq(rc_seq)

	extracted = extract_orfs(translated)
	extracted = list(set(extracted))

	for ex in extracted:
		print(ex)