# 상하좌우
import time

n = int(input())
plans = input().split()

start_time = time.time()

x, y = 1, 1
for plan in plans:
    if plan == 'L' and y > 1:
        y -= 1
    elif plan == 'R' and y < n:
        y += 1
    elif plan == 'U' and x > 1:
        x -= 1
    elif plan == 'D' and x < n:
        x += 1
print(f"{x} {y}")

print(f"time: {time.time() - start_time}")
