# 뱀
from sys import stdin
from queue import Queue

n = int(stdin.readline())
data = [[0] * n for _ in range(n)]

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    data[a - 1][b - 1] = 1

info = Queue()
for _ in range(int(stdin.readline())):
    x, c = stdin.readline().split()
    info.put((int(x), c))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # [Right, Down, Left, Up]

head_x, head_y, head_direction = 0, 0, 0
snake = Queue()
snake.put((head_x, head_y))
data[head_x][head_y] = 2

time = 0
x, c = info.get()
while True:
    if time == x:
        if c == 'L':
            head_direction = (head_direction - 1) % 4
        else:
            head_direction = (head_direction + 1) % 4
        if not info.empty():
            x, c = info.get()
            continue

    time += 1
    head_x, head_y = head_x + dx[head_direction], head_y + dy[head_direction]
    if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n or data[head_x][head_y] == 2:
        break

    if data[head_x][head_y] == 0:
        tail_x, tail_y = snake.get()
        data[tail_x][tail_y] = 0
    snake.put((head_x, head_y))
    data[head_x][head_y] = 2

print(time)

"""
입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
출력 예시 1
9

입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
출력 예시 2
21

입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
출력 예시 3
13
"""
