# 개미 전사
import time

input_1 = "4"
input_2 = "1 3 1 5"

start_time = time.time()

n = int(input_1)
array = list(map(int, input_2.split()))
array[2] += array[0]
for i in range(3, n):
    array[i] += max(array[i - 2], array[i - 3])
print(max(array[-2:]))

print(f"time: {time.time() - start_time}")
