# 반복문으로 구현한 이진 탐색 소스코드
"""
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 5 6 9 11 13 15 17 19
"""
import time

n, target = map(int, input().split())
array = list(map(int, input().split()))
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


result = binary_search(array, target, 0, n - 1)
if result:
    print(result + 1)
else:
    print("원소가 존재하지 않습니다.")
print(f"time: {time.time() - start_time}")
