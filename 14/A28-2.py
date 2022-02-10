# 고정점 찾기
from sys import stdin


def binary_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)


n, array = int(stdin.readline()), list(map(int, stdin.readline().split()))

print(binary_search(array, 0, n - 1))

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
