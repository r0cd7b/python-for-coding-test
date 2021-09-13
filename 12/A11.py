# 뱀
from sys import stdin
from queue import Queue

n = int(stdin.readline())
board = [[0] * n for _ in range(n)]

for _ in range(int(stdin.readline())):
    apple_x, apple_y = map(int, stdin.readline().split())
    board[apple_x - 1][apple_y - 1] = 1

information = Queue()
for _ in range(int(stdin.readline())):
    x, c = stdin.readline().split()
    information.put((int(x), c))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # [Up, Right, Down, Left]

head_x, head_y, head_direction = 0, 0, 1
snake = Queue()
snake.put((head_x, head_y))
board[head_x][head_y] = 2

time = 0
x, c = information.get()
while True:
    if time == x:
        if c == 'L':
            head_direction = (head_direction - 1) % 4
        else:
            head_direction = (head_direction + 1) % 4
        if not information.empty():
            x, c = information.get()
            continue

    time += 1
    head_x, head_y = head_x + dx[head_direction], head_y + dy[head_direction]
    if head_x < 0 or head_x >= n or head_y < 0 or head_y >= n or board[head_x][head_y] == 2:
        break

    snake.put((head_x, head_y))
    if board[head_x][head_y] == 0:
        tail_x, tail_y = snake.get()
        board[tail_x][tail_y] = 0
    board[head_x][head_y] = 2

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
