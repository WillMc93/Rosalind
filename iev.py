file = './datasets/rosalind_iev.txt'

def iev(file):

	data = list()

	with open(file) as inp:
		tmp = inp.readline()
		tmp.strip()

		data = tmp.split(' ')
		data = [float(d) for d in data]

	probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

	assert(len(probs) == len(data))

	dom_pop = 0.0
	for pop, prob in zip(data, probs):
		dom_pop += 2 * pop * prob

	return dom_pop

if __name__ == '__main__':
	print(iev(file))
