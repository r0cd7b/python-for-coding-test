# 정렬된 배열에서 특정 수의 개수 구하기
from sys import stdin
from bisect import bisect_right, bisect_left


def count_by_value(array, left_value, right_value):
    return bisect_right(array, right_value) - bisect_left(array, left_value)


n, x = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

count = count_by_value(array, x, x)
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
