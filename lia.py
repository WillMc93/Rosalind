from math import factorial as fac

k = 6
N = 17

P = 2**k

comb = lambda x, y: fac(x) / (fac(y) * fac(x - y))

prob = 0.0
for i in range(N, P+1):
	prob += comb(P, i) * (0.25**i) * (0.75**(P - i))

print(prob)