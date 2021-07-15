# 효율적인 화폐 구성
"""
2 15
2
3

3 4
3
5
7
"""
import time

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

start_time = time.time()

d = [0] + [10001] * m
for i in array:
    for j in range(i, m + 1):
        d[j] = min(d[j], d[j - i] + 1)
print(d[-1] if d[-1] <= 10000 else -1)

print(f"time: {time.time() - start_time}")
