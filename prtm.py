import re
import numpy as np

file_path = './datasets/rosalind_prtm.txt'
weight_file = './datasets/aa_monoisotopic_masses.txt'
weight_pattern = r'^(?P<sym>[A-Z])\s+(?P<weight>[0-9]+\.[0-9]+)$'

def build_weights(weight_file=weight_file, weight_pat=weight_pattern):
    weights = {}
    weight_pat = re.compile(weight_pat)

    with open(weight_file) as wf:
        for line in wf:
            weight_match = weight_pat.match(line)

            if weight_match:
                sym = weight_match.group('sym') 
                weight = weight_match.group('weight')
                weight = float(weight)
                weights[sym] = weight
   
    return weights

if __name__ == '__main__':
    seq = ''
    weights = build_weights()
    
    with open(file_path) as f:
        seq = f.readline()

    seq = seq.strip()
    print(seq)

    weight = 0.0
    for aa in seq:
        weight += weights[aa]

    print(np.round(weight, decimals=3))
