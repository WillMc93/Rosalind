from fasta_tools import fasta_read

file = './datasets/rosalind_gc.txt'

def gc_content(file):
	max_name = ''
	max_content = 0

	data = fasta_read(file)

	for name, seq in data.items():
		gc_count = 0
		gc_content = 0

		for bp in seq:
			if bp == 'G' or bp == 'C':
				gc_count += 1

		gc_content = gc_count / len(seq) * 100

		if gc_content > max_content:
			max_name = name
			max_content = gc_content


	return max_name, max_content

if __name__ == '__main__':
	name, content = gc_content(file)
	print(name + '\n' + str(content))


