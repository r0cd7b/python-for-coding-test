# 피보나치 수열 소스코드 (반복적)
import time

start_time = time.time()

d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])

print(f"time: {time.time() - start_time}")
