# 소수 구하기
from sys import stdin
from math import sqrt

m, n = map(int, stdin.readline().split())

prime = [True] * (n - 1)
for i in range(2, int(sqrt(n)) + 1):
    j = i * 2
    while j <= n:
        prime[j - 2], j = False, i + j

for i in range(m - 2, n - 1):
    if prime[i]:
        print(i + 2)

"""
입력 예시
3 16
출력 예시
3
5
7
11
13
"""
