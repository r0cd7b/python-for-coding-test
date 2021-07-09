# 왕실의 나이트
import time

input_data = input()

start_time = time.time()

column = ord(input_data[0]) - ord('a') + 1
row = int(input_data[1])
result = 0
if column > 1:
    if row > 2:
        result += 1
    if row < 7:
        result += 1
if column < 8:
    if row > 2:
        result += 1
    if row < 7:
        result += 1
if row > 1:
    if column > 2:
        result += 1
    if column < 7:
        result += 1
if row < 8:
    if column > 2:
        result += 1
    if column < 7:
        result += 1
print(result)

print(f"time: {time.time() - start_time}")
