#!/usr/bin/python2

import matplotlib.pyplot as plt
import sys
import fileinput
import os.path
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

if len(sys.argv) < 3:
  print("usage: xyz_file point_index [max]")
  print("Allow to visualise furthest point sampling")
  exit(0)

xyz = sys.argv[1]
point_index = int(sys.argv[2])
nb = 10
if (len(sys.argv) > 3):
  nb = int(sys.argv[3])

def dist(p, q):
  (x1, y1, z1) = p
  (x2, y2, z2) = q
  (x, y, z) = (x1-x2, y1-y2, z1-z2)
  return math.sqrt(x*x + y*y + z*z)

pt = []
for line in open(xyz):
  (x, y, z) = line.split()
  pt.append((float(x), float(y), float(z)))

pt2 = [pt[point_index]]
def argmin(iterable):
    return min(enumerate(iterable), key=lambda x: x[1])[0]
def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

while len(pt2) < len(pt) and len(pt2) <= nb:
  d = {}
  # Compute dist(v, pt2) for all v in pt \ pt2
  for v in set(pt) - set(pt2):
    d[v] = dist(v, pt2[0])
    for w in pt2[1:]:
       d[v] = min(d[v], dist(v, w))
  # Find the index of the farthest v
  inverse = [(value, key) for key, value in d.items()]
  next_pt = max(inverse)[1]
  pt2.append(next_pt)


pt2 = pt2[:nb]
print(pt2)

colors = []
for i in range(0, len(pt2)):
  colors.append(255.0 * i / float(len(pt2)))

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = plt.subplot(111)
x = list(map(lambda x: x[0], pt2))
y = list(map(lambda x: x[1], pt2))
z = list(map(lambda x: x[2], pt2))
#print(pt)
ax.scatter(x, y, c=colors, zorder=2)
plt.show()
