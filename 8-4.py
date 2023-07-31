# 바닥 공사
from sys import stdin

n = int(stdin.readline())

floor = [1, 3]
for i in range(2, n):
    floor.append((floor[i - 2] * 2 + floor[i - 1]) % 796796)

print(floor[n - 1])
'''
3

5
'''
