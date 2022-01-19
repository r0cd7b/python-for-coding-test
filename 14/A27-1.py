# 정렬된 배열에서 특정 수의 개수 구하기
from sys import stdin

n, x = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

endpoint = n - 1
start, end, count = 0, endpoint, -1
while start <= end:
    midpoint = (start + end) // 2
    if x == sequence[midpoint]:
        if count == -1:
            if midpoint == endpoint or x != sequence[midpoint + 1]:
                start, end, count = 0, endpoint, midpoint
            else:
                start = midpoint + 1
        else:
            if midpoint == 0 or x != sequence[midpoint - 1]:
                count -= midpoint - 1
                break
            else:
                end = midpoint - 1
    elif x > sequence[midpoint]:
        start = midpoint + 1
    else:
        end = midpoint - 1

print(count)

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
