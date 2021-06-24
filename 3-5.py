# 1이 될 때까지
import time

n, k = map(int, input().split())

start_time = time.time()

result = 0
while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    result += 1
print(result)

print(f"time: {time.time() - start_time}")
