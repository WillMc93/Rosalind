file = './datasets/rosalind_hamm.txt'

def hamming(file):
	seq1, seq2 = '', ''
	diff = 0

	with open(file) as f:
		seq1 = f.readline()
		seq2 = f.readline()

	for x,y in zip(seq1, seq2):
		if x != y:
			diff += 1

	return diff

if __name__ == '__main__':
	print(hamming(file))
