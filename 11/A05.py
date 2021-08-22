# 볼링공 고르기
"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
array = [0] * m
for k in stdin.readline().split():
    array[int(k) - 1] += 1
result = 0
for i in range(m):
    n -= array[i]
    result += n * array[i]
print(result)
