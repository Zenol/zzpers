#!/usr/bin/python2

from dionysus import *
import sys
import os.path
import glob

if (len(sys.argv)) < 2:
  print("usage: folder/ selected_barcode")
  print("Compute the bottleneck distance beetwen barcode stored in all the files of foler")
  exit(0)

folder = sys.argv[1]
ifile = sys.argv[2]

def unsafe_file_name(i):
    name = os.path.basename(i)
    return name.split('.')[0]

def load_pers(file):
    dia = PersistenceDiagram(1)
    f = open(file)
    for line in f:
        (dim, b, d) = line.split(' ')
        dia.append((float(b), float(d)))
    # !!! Dionysus crash with empty diagrams !!!
    return dia

p1 =     load_pers(ifile)
for i in glob.glob(folder + '/*.pers'):
    if not os.path.isfile(i):
      continue
    p2 = load_pers(i)
    print unsafe_file_name(ifile), unsafe_file_name(i), bottleneck_distance(p1, p2)

