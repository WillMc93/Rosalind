from fasta_tools import fasta_read
from itertools import product

file = './datasets/rosalind_grph.txt'

def grph(file, k=3):
	data = fasta_read(file)

	matches = list()

	for itm1, itm2 in product(data.items(), repeat=2):

		(name1, seq1), (name2, seq2) = itm1, itm2

		if name1 == name2 or seq1 == seq2:
			continue

		else:
			if seq1[-k:] == seq2[:k]:
				matches.append((name1, name2))

	return matches

if __name__ == '__main__':
	matches = grph(file)

	#matches = sorted(matches, key=lambda match: match[0])

	with open('./outputs/rosalind_grph.txt', 'w') as outp:
		for match in matches:
			out = str(match[0]) + ' ' + str(match[1] + '\n')
			outp.write(out)
					