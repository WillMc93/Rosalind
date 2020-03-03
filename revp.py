from fasta_tools import fasta_read, just_seq

file_path = './datasets/rosalind_revp.txt'

def reverse_compliment(seq):
	compliments = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

	seq = seq[::-1]
	rc = ''
	for i in range(len(seq)):
		rc += compliments[seq[i]]

	return rc

def find_palindromes(seq, min_len=4, max_len=12):
    # UHHH, were going to brute-force it, George!
    palindromes = []

    for length in range(min_len, max_len+1):
        for idx in range(0, len(seq)-length+1):
            sub_seq = seq[idx:idx+length]
            rc_sub_seq = reverse_compliment(sub_seq)

            if sub_seq == rc_sub_seq:
                palindromes.append((idx+1, length))

    return palindromes

if __name__ == '__main__':
    data = fasta_read(file_path)
    data = just_seq(data)

    palindromes = []
    for seq in data:
        palindromes = find_palindromes(seq)

    palindromes = sorted(palindromes, key=lambda pair: pair[0])
    for loc, length in palindromes:
        print(f"{loc} {length}")


