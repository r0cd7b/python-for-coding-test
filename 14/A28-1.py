# 고정점 찾기
from sys import stdin

n, elements = int(stdin.readline()), list(map(int, stdin.readline().split()))

start, end = 0, n - 1
while start <= end:
    midpoint = (start + end) // 2
    if elements[midpoint] == midpoint:
        print(elements[midpoint])
        break
    elif elements[midpoint] < midpoint:
        start = midpoint + 1
    else:
        end = midpoint - 1
else:
    print(-1)

"""
입력 예시 1
5
-15 -6 1 3 7
출력 예시 1
3

입력 예시 2
7
-15 -4 2 8 9 13 15
출력 예시 2
2

입력 예시 3
7
-15 -4 3 8 9 13 15
출력 예시 3
-1
"""
