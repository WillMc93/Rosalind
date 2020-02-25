from fasta_tools import fasta_read

import numpy as np

file = './datasets/rosalind_lcsm.txt'

def lcsm(file):

	# get sequences/IDs
	data = fasta_read(file)

	# reduce to only sequences
	data = [seq for _, seq in data.items()]

	subs = list()

	first = data[0]

	# get every substring of the first entry
	for i in range(0, len(first)):
		for j in range(2, len(first) + 1):
			if len(first[i:j]) < 2:
				continue
			if first[i:j] not in data[1]:
				break

			if first[i:j] not in subs:
				print(f'{len(subs)}: {first[i:j]}')
				subs.append(first[i:j])

	# find the longest commons substring
	subs_temp = subs.copy()

	for sub in subs:
		for seq in data[2:]:
			if sub not in seq:
				subs_temp.remove(sub)
				break

	subs = subs_temp
	if len(subs) == 1:
		return subs[0]

	subs = sorted(subs, key=len)

	return subs[-1]				

if __name__ == '__main__':
	print(str(lcsm(file)))	