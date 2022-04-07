# 아기 상어
from sys import stdin
from collections import deque


def move(size_, eaten_):
    if not visits[x][y] and space[x][y] <= size_:
        visits[x][y] = True
        queue.append((x, y))
        if space[x][y] >= 1:
            eaten_ += 1
            if size_ <= eaten_:
                size_, eaten_ = size + 1, 0
    return size_, eaten_


n, space, position = int(stdin.readline()), [], None
for i in range(n):
    space.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        if space[i][j] == 9:
            position = (i, j)

eaten, visits, size, queue = 0, [[False] * n for _ in range(n)], 2, deque()
while True:
    x, y = position[0] - 1, 0
    if x >= 0:
        size, eaten = move(size, eaten)
    x, y = position[0] + 1, 0
    if x < n:
        size, eaten = move(size, eaten)
    x, y = 0, position[1] - 1
    if y >= 0:
        size, eaten = move(size, eaten)
    x, y = 0, position[1] + 1
    if y < n:
        size, eaten = move(size, eaten)
    if not queue:
        break
    position = queue.popleft()

"""
입력 예시 1
3
0 0 0
0 0 0
0 9 0
출력 예시 1
0

입력 예시 2
3
0 0 1
0 0 0
0 9 0
출력 예시 2
3

입력 예시 3
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
출력 예시 3
14
"""
