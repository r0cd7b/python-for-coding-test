from sys import stdin


def binary_search(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    if target < array[mid]:
        return binary_search(start, mid - 1)
    return binary_search(mid + 1, end)


# def binary_search(start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == array[mid]:
#             return mid
#         if target > array[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1


n, target = stdin.readline().split()
n, target, array = int(n), int(target), [int(s) for s in stdin.readline().split()]

result = binary_search(0, n - 1)
if result >= 0:
    print(result + 1)
else:
    print(result)
'''
10 7
1 3 5 7 9 11 13 15 17 19

4


10 7
1 3 5 6 9 11 13 15 17 19

-1
'''
