from rna_table import codon_lookup

file = './datasets/rosalind_mrna.txt'

def calculate(polypep):
	# add stop codon
	polypep += '*'

	combos = 1
	for aa in polypep:
		combos *= len(codon_lookup(aa))
		combos = combos % int(1e6)

	return combos


if __name__ == '__main__':
	polypep = ''
	with open(file) as f:
		polypep = f.readline().strip()

	print(calculate(polypep))