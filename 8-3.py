# 개미 전사
from sys import stdin

n = int(stdin.readline())
k: list = list(map(int, stdin.readline().split()))

if k[0] > k[1]:
    k[1] = k[0]
for i in range(2, n):
    a = k[i] + k[i - 2]
    b = k[i - 1]
    k[i] = a if a > b else b

print(k[-1])
'''
4
1 3 1 5

8
'''
