# 소수 구하기
from sys import stdin
from math import sqrt

m, n = map(int, stdin.readline().split())

prime = [False] + [True] * (n - 1)
for i in range(1, int(sqrt(n))):
    if prime[i]:
        i += 1
        j = i * 2
        while j <= n:
            prime[j - 1], j = False, i + j

for i in range(m - 1, n):
    if prime[i]:
        print(i + 1)

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
