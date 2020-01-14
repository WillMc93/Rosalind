import pdb

def fibd(n, m):
	rabbits = [['b', 0]]

	for i in range(0, n):
		# oh they faukin
		rabbits_  = rabbits
		for rabbit in rabbits:
			if rabbit[0] == 'a':
				rabbits_.append(['b', 0])

		rabbits = rabbits_
		
		# increment age
		for rabbit in rabbits:
			rabbit[1] += 1

		# age babies
		for rabbit in rabbits:
			if rabbit == ['b', 2]:
				rabbit[0] = 'a'

		# kill'em
		rabbits_ = []
		for rabbit in rabbits:
			if rabbit[1] <= m:
				rabbits_.append(rabbit)

		rabbits = rabbits_

		print(i)

	return len(rabbits)


print(fibd(92, 16))
