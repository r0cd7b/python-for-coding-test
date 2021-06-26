# 시각
import time

n = int(input())

start_time = time.time()

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

print(f"time: {time.time() - start_time}")
