#!/usr/bin/python3

import random
import math

sz = 400

pts = []
for i in range(0, sz):
    pts.append((random.uniform(-100, 100), random.uniform(-100, 100), i/20000.0))

def mykey(u):
    (x, y, z) = u
    return math.sqrt(x*x+y*y+z*z)

pts.sort(key=mykey)

for p in pts:
    (x, y, z) = p
    print("{} {} {}".format(x, y, z))



