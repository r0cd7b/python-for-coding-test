# 상하좌우
import time

n = int(input())
plans = input().split()

start_time = time.time()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    nx = x
    ny = y
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx += dx[i]
            ny += dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(f"{x} {y}")

print(f"time: {time.time() - start_time}")
