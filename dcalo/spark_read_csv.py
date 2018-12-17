import os

os.chdir('./')
print (os.getcwd())

import pandas as pd
file_csv = pd.read_csv('usuarios_win_mac_lin.csv', delimiter=",")
file_csv
file_csv.describe

cell = file_csv.loc[1, ['acciones']].values[0]
print (cell)

# FNA FILE
#for record in SeqIO.parse("fichero2.fna", "fasta"):
#    print(record.seq)

#for record in SeqIO.parse("fichero2.fna", "fasta"):
#    print(record.description)


import glob, pprint
genomes = glob.glob('../viral/*.fna.gz')
genomes = list(sorted(genomes))

pprint.pprint(genomes)

import screed

for g in genomes:
    for record in screed.open(g):
        print(record.sequence[:5])


import urllib.request as p
path=p.urlopen('http://humanstxt.org/humans.txt')
fileFinal=path.read()
fileFinal

import urllib.request as p
path=p.urlopen('http://files.rcsb.org/download/101m.pdb')
fileFinal=path.read()
fileFinal