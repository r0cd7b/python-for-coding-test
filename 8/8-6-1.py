# 개미 전사
import time

input_1 = "8"
input_2 = "5 4 0 2 3 2 8 2"

start_time = time.time()

n = int(input_1)
array = list(map(int, input_2.split()))
array[2] += array[0]
for i in range(3, n):
    array[i] += max(array[i - 2], array[i - 3])
print(max(array[-2:]))

print(f"time: {time.time() - start_time}")
