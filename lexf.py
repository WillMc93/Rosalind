from itertools import product

path = './datasets/rosalind_lexf.txt'
outp = './outputs/rosalind_lexf.out'

if __name__ == '__main__':
    alphabet = ''
    length = 0

    with open(path) as f:
        alphabet = f.readline()
        alphabet = alphabet.strip()
        alphabet = alphabet.split(' ')

        length = f.readline()
        length = length.strip()
        length = int(length)

    open(outp, 'w').close()

    for prod in product(alphabet, repeat=length):
        prod = ''.join(prod)
        print(prod)

        with open(outp, 'a') as f:
            f.write(prod)
            f.write('\n')

