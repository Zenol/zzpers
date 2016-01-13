#!/usr/bin/python3

sz = 80


#           /
#          /
# |--------
#          \
#           \


for i in range(0, 20):
    print("{} {} {}".format(-1.01, 1/2 - i/float(20), 0))


for i in range(0, sz + 1):
    print("{} {} {}".format(-1.0+i/float(sz), 0, 0))

for i in range(1, sz):
    print("{} {} {}".format(i/float(sz), i/float(sz), 0))
for i in range(1, sz):
    print("{} {} {}".format(i/float(sz), i/float(sz), 0.2))

for i in range(1, sz):
    print("{} {} {}".format(i/float(sz), -i/float(sz), 0))



