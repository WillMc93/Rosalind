path = './datasets/rosalind_lgis.txt'
outp = './outputs/rosalind_lgis.out'

def sub(permutation):

    max_sub = []

    for i in permutation:
        temp_sub = permutation[i]

def recurse(permutation, sub, 

if __name__ == '__main__':
    
    inc_comp = lambda a, b: a < b
    dec_comp = lambda a, b: a > b
    
    size = 0
    permutation = []
    with open(path) as f:
        size = f.readline()
        size = size.strip()
        size = int(size)

        permutation = f.readline()
        permutation = permutation.strip()
        permutation = permutation.split(' ')
        permutation = [int(i) for i in permutation]

    assert(size == len(permutation))

    inc_sub = sub(permutation, inc_comp)
    dec_sub = sub(permutation, dec_comp)

    inc_sub_str = ''
    dec_sub_str = ''

    for i in inc_sub:
        inc_sub_str += str(i) + ' '
    inc_sub_str += '\n'

    for i in dec_sub:
        dec_sub_str += str(i) + ' '
    dec_sub_str += '\n'

    with open(outp, 'w') as f:
        f.write(inc_sub_str)
        f.write(dec_sub_str)

