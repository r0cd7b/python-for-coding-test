# 1로 만들기
import time

input_1 = input()

start_time = time.time()

x = int(input_1)
d = [0] * 30001
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])

print(f"time: {time.time() - start_time}")
