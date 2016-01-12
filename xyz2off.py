import fileinput

l = []
for line in fileinput.input():
    l.append(line)

print('OFF')
print('{0} {0} 0'.format(len(l)))

for line in l:
    print(line, end='')

for i in range(0, len(l)):
    print('1 {}'.format(i))
