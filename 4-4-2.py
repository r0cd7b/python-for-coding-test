# 게임 개발
import time

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

start_time = time.time()


def turn_left():
    global direction
    direction = (direction - 1) % 4


array[x][y] = -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
count = 1
turn_time = 0
while True:
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]
    if array[nx][ny] == 0:
        array[nx][ny] = -1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    turn_time += 1
    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        else:
            break
print(count)

print(f"time: {time.time() - start_time}")
