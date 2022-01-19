# 정렬된 배열에서 특정 수의 개수 구하기
from sys import stdin

n, x = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

start, end, first = 0, n - 1, 2
while start <= end:
    midpoint = (start + end) // 2
    if x > sequence[midpoint]:
        start = midpoint + 1
    elif sequence[midpoint] == x > sequence[midpoint - 1]:
        first = midpoint
        break
    else:
        end = midpoint - 1
start, end, last = 0, n - 1, 0
while start <= end:
    midpoint = (start + end) // 2
    if x < sequence[midpoint]:
        end = midpoint - 1
    elif sequence[midpoint] == x < sequence[midpoint + 1]:
        last = midpoint
        break
    else:
        start = midpoint + 1

print(last - first + 1)

"""
입력 예시 1
7 2
1 1 2 2 2 2 3
출력 예시 1
4

입력 예시 2
7 4
1 1 2 2 2 2 3
출력 예시 2
-1
"""
