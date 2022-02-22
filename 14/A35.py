# 못생긴 수
from sys import stdin

n = int(stdin.readline())

ugly, next2, next3, next5, i2, i3, i5 = [1], 2, 3, 5, 0, 0, 0
for i in range(1, n):
    ugly.append(min(next2, next3, next5))
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[-1])

"""
입력 예시 1
10
출력 예시 1
12

입력 예시 2
4
출력 예시 2
4
"""
