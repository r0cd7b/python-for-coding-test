# 개미 전사
import time

input_1 = "4"
input_2 = "1 3 1 5"

start_time = time.time()

n = int(input_1)
array = list(map(int, input_2.split()))
array[1] = max(array[0], array[1])
for i in range(2, n):
    array[i] = max(array[i - 1], array[i] + array[i - 2])
print(array[-1])

print(f"time: {time.time() - start_time}")
