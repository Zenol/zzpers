#!/usr/bin/python2

import matplotlib.pyplot as plt
import sys
import fileinput
import os.path
import math
import numpy as np

if len(sys.argv) < 3:
  print("usage: xyz_file point_index bottleneck_dist_file")
  print("Take in stdin a xyz file, and compute the distance from"
        "point point_index to others points");
  exit(0)

xyz = sys.argv[1]
point_index = int(sys.argv[2])
bottleneck_file = sys.argv[3]

def dist(p, q):
  (x1, y1, z1) = p
  (x2, y2, z2) = q
  (x, y, z) = (x1-x2, y1-y2, z1-z2)
  return math.sqrt(x*x + y*y + z*z)

pt = []
for line in open(xyz):
  (x, y, z) = line.split()
  pt.append((float(x), float(y), float(z)))

# Compute a list of [first_point second_point distance]
# The list is sorted by index of points
pts_l = []

for i in range(0, len(pt)):
  if i == point_index:
    continue
  pts_l.append([i, dist(pt[point_index], pt[i])])

# Read the bottleneck distance list
# sorted by index

diag_l = []
for line in open(bottleneck_file):
  (x, y, z) = line.split()
  if x != y: # Remove the case x == y, where dist = 0
    diag_l.append([int(y), float(z)])
diag_l.sort(key=lambda a: a[0])


# Test : check that all index of those two list are the same
#        otherwise throw.
def eq(a):
  (x, y) = a
  return x[0] != y[0]

check = filter(eq, zip(pts_l, diag_l))
if len(check) != 0:
  print(check)
  print("Mismatch bottleneck and points index!!!")
  exit(1)

diag_l = map(lambda a: a[1], diag_l)
pts_l = map(lambda a: a[1], pts_l)

colors = []
for i in range(0, len(diag_l)):
  colors.append(255.0 * i / float(len(diag_l)))
print colors
print len(pts_l), len(diag_l)
plt.scatter(pts_l, diag_l, c=colors)
plt.show()
