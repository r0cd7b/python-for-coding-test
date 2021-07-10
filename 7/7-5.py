"""
부품 찾기 (이진 탐색)

5
8 3 7 9 2
3
5 7 9
"""
import time

start_time = time.time()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


n = int("5")
array = list(map(int, "8 3 7 9 2".split()))
array.sort()
m = int("3")
x = list(map(int, "5 7 9".split()))
for i in x:
    if binary_search(array, i, 0, n - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
print(f"\ntime: {time.time() - start_time}")
