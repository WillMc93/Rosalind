# http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/

class tables:
	def __init__(self):
		bases = "tcag"
		codons = [a + b + c for a in bases for b in bases for c in bases]
		amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
		
		self.codon_to_acid = dict(zip(codons, amino_acids))

		self.acid_to_codon = dict()
		for codon, acid in self.codon_to_acid.items():
			if acid in self.acid_to_codon:
				self.acid_to_codon[acid].append(codon)
			else:
				self.acid_to_codon[acid] = [codon]

tables = tables()

def acid_lookup(codon, tables=tables):
	acid = ''
	try:
		acid = tables.codon_to_acid[codon]
	except KeyError:
		acid = acid

	return acid

def codon_lookup(acid, tables=tables):
	codons = [None]

	try:
		codons = tables.acid_to_codon[acid]
	except KeyError:
		codons = codons

	return codons