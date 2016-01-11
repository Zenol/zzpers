#!/usr/bin/python2

import matplotlib.pyplot as plt
import sys
import fileinput
import math

def dist(p, q):
  (x1, y1, z1) = p
  (x2, y2, z2) = q
  (x, y, z) = (x1-x2, y1-y2, z1-z2)
  return math.sqrt(x*x + y*y + z*z)

if len(sys.argv) < 2:
  print("usage: point_index")
  print("Take in stdin a xyz file, and compute the distance from"
        "point point_index to others points");
  exit(0)

pt = []
for line in sys.stdin:
  (x, y, z) = line.split()
  pt.append((float(x), float(y), float(z)))

# Compute a list of [first_point second_point distance]
l = []
point_index = int(sys.argv[1])
for i in range(0, len(pt)):
  if i == point_index:
    continue
  l.append([point_index, i, dist(pt[point_index], pt[i])])

# Sort the list l
def get_dist(a):
  [_, _, z] = a
  return z
l.sort(key=get_dist)

# Print the list l
for v in l:
  [a, b, c] = v
  print a, b, c
