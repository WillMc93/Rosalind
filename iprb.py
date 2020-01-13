file = './datasets/rosalind_IPRB.txt'

from itertools import combinations

def iprb(file):
	k,m,n = [0]*3

	with open(file) as f:

		data = f.readline()
		data.strip()

		k,m,n = data.split(' ')

	total = 2 * (k + m + n)

	assert(total > 0)

	k_prob = 2*k / total
	m_prob = m / total
	n_prob = n / total

	total_prob = 0

	for prob1, prob2 in combinations([k_prob, m_prob, n_prob]):


