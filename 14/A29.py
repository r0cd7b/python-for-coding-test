# 공유기 설치
from sys import stdin

n, c = map(int, stdin.readline().split())
x = sorted([int(stdin.readline()) for _ in range(n)])

start, end, distance = 1, x[-1] - x[1], 0
while start <= end:
    midpoint = (start + end) // 2
    for i in range(len(x) - c):
        previous, router = x[i], c - 1
        for j in range(i + 1, len(x)):
            if x[j] - previous >= midpoint:
                if router <= 1:
                    break
                previous, router = x[j], router - 1
        else:
            continue
        break
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
