from itertools import permutations
import sys
import math

def permutate(n):
    nums = [] 
    perms = []

    for i in range(1, n+1):
        nums.append(i)

    assert(len(nums) == n)

    for perm in permutations(nums, n):
        perms.append(perm)

    assert(math.factorial(n) == len(perms))

    return len(perms), perms

n = sys.argv[1]
n = int(n)

p, perms = permutate(n)
print(p)
for perm in perms:
    outp = ''
    for num in perm:
        outp += str(num) + ' '

    print(outp)
