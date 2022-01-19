# 정렬된 배열에서 특정 수의 개수 구하기
from sys import stdin
from bisect import bisect_right, bisect_left

n, x = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

count = bisect_right(sequence, x) - bisect_left(sequence, x)

print(count if count else -1)

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
