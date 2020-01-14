file = './datasets/rosalind_subs.txt'

s = ''
t = '' 

with open(file) as f:
	s = f.readline().strip()
	t = f.readline().strip()
	
slices = [s[i:i+len(t)] for i in range(len(s) - len(t))]
	
hits = []
for idx, slc in enumerate(slices):
	if slc == t:
		hits.append(idx+1)
		
outp = ''
for hit in hits:
	outp += str(hit) + ' '
print(outp)
	