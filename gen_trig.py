#!/usr/bin/python3

sz = 80


#           /
#          /
# |--------
#          \
#           \


for i in range(1, sz):
    print("{} {} {}".format(i/float(sz), 0, 0))

for i in range(1, sz):
    print("{} {} {}".format(1.0 - i/float(sz)/2.0, i/float(sz), 0.001))

for i in range(1, sz):
    print("{} {} {}".format(0.5 - i/float(sz)/2.0, 1 - i/float(sz), 0.002))


