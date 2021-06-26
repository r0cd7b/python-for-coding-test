# 왕실의 나이트
import time

input_data = input()

start_time = time.time()

column = ord(input_data[0]) - ord('a') + 1
row = int(input_data[1])
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
result = 0
for step in steps:
    next_column = column + step[0]
    next_row = row + step[1]
    if 1 <= next_column <= 8 and 1 <= next_row <= 8:
        result += 1
print(result)

print(f"time: {time.time() - start_time}")
