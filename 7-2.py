from sys import stdin

stdin.readline()
parts = [False] * 999999
for part in stdin.readline().split():
    parts[int(part) - 1] = True
stdin.readline()
customer = list(map(int, stdin.readline().split()))

for part in customer:
    if parts[part - 1]:
        print('yes', end=' ')
    else:
        print('no', end=' ')

'''
5
8 3 7 9 2
3
5 7 9

no yes yes
'''
