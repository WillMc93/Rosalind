from fasta_tools import fasta_read
import re
from codon_tables import acid_lookup

file_path = './datasets/rosalind_splc.txt'

def init(path=file_path):
    # laziness means more work but so be it
    # read in as we normally do
    data = fasta_read(path)

    # get the data into list (subs)
    master = ''
    subs = []
    for name, seq in data.items():
        subs.append((name, seq))

    # make sure list is sorted longest seq to shortest
    subs = sorted(subs, key=lambda pair: len(pair[1]))
    subs = subs[::-1]

    # pull off longest as the master sequence
    master = subs[0]
    master = master[1]
    subs = subs[1::]

    # dissolve sub tuples (keep seq)
    for idx, sub in enumerate(subs):
        subs[idx] = sub[1]

    return master, subs

def remove_introns(master, subs):

    for sub in subs:
        master = re.sub(sub, '---', master)

    master = re.sub(r'---', '', master)

    return master

def translate(master):
    outp = ''
    for i in range(0, len(master), 3):
        codon = master[i:i+3]
        aa = acid_lookup(codon)
        if aa == '*':
            continue

        outp += aa

    return outp

if __name__ == '__main__':
    master, subs = init()

    master = remove_introns(master, subs)

    outp = translate(master)

    print(outp)
