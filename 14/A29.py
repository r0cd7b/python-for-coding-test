# 공유기 설치
from sys import stdin

n, c = map(int, stdin.readline().split())
x = sorted([int(stdin.readline()) for _ in range(n)])

start, end, distance = 1, x[-1] - x[0], 0
while start <= end:
    current, midpoint, routers = x[0], (start + end) // 2, 1
    for i in range(1, n):
        if x[i] - current >= midpoint:
            routers += 1
            if c <= routers:
                break
            current = x[i]
    else:
        end = midpoint - 1
        continue
    start, distance = midpoint + 1, midpoint

print(distance)

"""
입력 예시
5 3
1
2
8
4
9

출력 예시
3
"""
