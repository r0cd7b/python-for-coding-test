# 큰 수의 법칙
import time

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

data.sort(reverse=True)
result = (data[0] * k + data[1]) * (m // (k + 1)) + data[0] * (m % (k + 1))
print(result)

print(f"time: {time.time() - start_time}")
