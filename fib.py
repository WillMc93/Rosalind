# I couldn't understand the problem declaration, so I found this :(
# https://github.com/kaniick/Rosalind/blob/master/Bioinformatics%20Stronghold/Rabbits%20and%20Recurrence%20Relations%20(FIB)

def fib(n, k):

	if n == 0:
		return 0

	elif n == 1:
		return 1

	f1 = fib(n-1, k)
	f2 = k * fib(n-2, k)

	return f1 + f2

if __name__ == '__main__':
	print(fib(31, 4)) 