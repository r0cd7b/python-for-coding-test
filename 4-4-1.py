# 게임 개발
import time

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

start_time = time.time()

array[x][y] = -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
count = 1
while True:
    for i in range(4):
        direction = (direction - 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
            array[x][y] = -1
            count += 1
            break
    else:
        nx, ny = x - dx[direction], y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
print(count)

print(f"time: {time.time() - start_time}")
