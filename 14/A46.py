# 아기 상어
from sys import stdin
from collections import deque


def initial_append(_x, _y):
    _distances = [[longest] * n for _ in range(n)]
    _distances[_x][_y], space[_x][_y] = 0, 0
    omnidirectional_append(_x, _y, _distances)
    return _distances


def omnidirectional_append(_x, _y, _distances):
    x_next = _x - 1
    if x_next >= 0:
        append(x_next, _y, _distances, _distances[_x][_y])
    x_next = _x + 1
    if n > x_next:
        append(x_next, _y, _distances, _distances[_x][_y])
    y_next = _y - 1
    if y_next >= 0:
        append(_x, y_next, _distances, _distances[_x][_y])
    y_next = _y + 1
    if n > y_next:
        append(_x, y_next, _distances, _distances[_x][_y])


def append(_x, _y, _distances, _distance_previous):
    if _distances[_x][_y] >= longest and space[_x][_y] <= size:
        bfs.append((_x, _y))
        _distances[_x][_y] = _distance_previous + 1


n, distances = int(stdin.readline()), None
space, longest, size, bfs = [list(map(int, stdin.readline().split())) for _ in range(n)], n ** 2, 2, deque()
for i in range(n):
    for j in range(n):
        if space[i][j] >= 9:
            distances = initial_append(i, j)
            break
    else:
        continue
    break
eaten, elapsed = 0, 0
while True:
    while bfs:
        x, y = bfs.popleft()
        omnidirectional_append(x, y, distances)
    shortest, x, y = longest, None, None
    for i in range(n):
        for j in range(n):
            if distances[i][j] < shortest and size > space[i][j] >= 1:
                shortest, x, y = distances[i][j], i, j
    if shortest >= longest:
        break
    eaten += 1
    if size <= eaten:
        size, eaten = size + 1, 0
    elapsed, distances = elapsed + shortest, initial_append(x, y)
print(elapsed)

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
