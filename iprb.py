"""
The dumbest way to do this.
I'm 100% sure there is a numerical solution, but I'm too stupid right now.
"""

file = './datasets/rosalind_IPRB.txt'

from itertools import combinations


def mendel(p1, p2, results=list()):
	if p1 == 'k' or p2 == 'k':
		results += ['dom'] * 4

	elif p1 == 'm' and p2 == 'm':
		results += ['dom'] * 3 + ['rec']

	elif p1 == 'm' and p2 == 'n':
		results += ['dom'] * 2 + ['rec'] * 2

	elif p1 == 'n' and p2 == 'n':
		results += ['rec'] * 4

	else:
		mendel(p2, p1, results)

	return results


def iprb(file):
	k,m,n = [0]*3

	population = list()
	total = 0

	with open(file) as f:

		data = f.readline()
		data.strip()

		k,m,n = [int(x) for x in data.split(' ')]

		population = ['k'] * k + ['m'] * m + ['n'] * n
		total = k + m + n

	results = list()
	for p1, p2 in combinations(population, 2):
		results = mendel(p1, p2, results)

	doms = 0
	for off in results:
		if off == 'dom':
			doms += 1

	return doms/len(results)

if __name__ == '__main__':
	print(iprb(file))
