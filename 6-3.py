# 두 배열의 원소 교체
from sys import stdin

_, k = stdin.readline().split()
a = [int(element) for element in stdin.readline().split()]
b = [int(element) for element in stdin.readline().split()]

a.sort()
b.sort(reverse=True)
for i in range(int(k)):
    if a[i] >= b[i]:
        break
    a[i] = b[i]

print(sum(a))
'''
5 3
1 2 5 4 3
5 5 6 6 5

26
'''
