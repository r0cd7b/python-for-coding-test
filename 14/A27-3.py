# 정렬된 배열에서 특정 수의 개수 구하기
from sys import stdin


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    mid_previous = mid - 1
    if array[mid] == target:
        if mid == 0 or array[mid_previous] < target:
            return mid
        else:
            return first(array, target, start, mid_previous)
    elif array[mid] < target:
        return first(array, target, mid + 1, end)
    else:
        return first(array, target, start, mid_previous)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    mid_next = mid + 1
    if array[mid] == target:
        if mid == 0 or array[mid_next] > target:
            return mid
        else:
            return last(array, target, mid_next, end)
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid_next, end)


def count_by_value(array, x):
    n = len(array) - 1
    b = last(array, x, 0, n)
    if b:
        return b - first(array, x, 0, n) + 1
    return -1


n, x = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

print(count_by_value(array, x))

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
