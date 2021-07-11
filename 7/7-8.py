"""
떡볶이 떡 만들기

4 6
19 15 10 17
"""
import time

start_time = time.time()
n, m = map(int, "4 6".split())
array = list(map(int, "19 15 10 17".split()))

result = 0
start = 0
end = max(array)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
print(f"time: {time.time() - start_time}")
