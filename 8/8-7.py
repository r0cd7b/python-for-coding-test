# 바닥 공사
import time

input_1 = "100"

start_time = time.time()

n = int(input_1)
d = [0] * n
d[0] = 1
d[1] = d[0] + 2
for i in range(2, n):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796
print(d[-1])

print(f"time: {time.time() - start_time}")
