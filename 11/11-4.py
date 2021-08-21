# 만들 수 없는 금액
"""
5
3 2 1 1 9
"""
from sys import stdin

n = int(stdin.readline()[:-1])
data = list(map(int, stdin.readline().split()))
data.sort()
target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)
