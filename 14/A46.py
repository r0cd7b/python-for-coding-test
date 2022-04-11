# 아기 상어
from sys import stdin
from copy import deepcopy
from collections import deque


def omnidirectional_append(x_, y_):
    next_, distance = x_ - 1, distances[x_][y_] + 1
    if next_ >= 0:
        append(next_, y_, distance)
    next_ = x_ + 1
    if n > next_:
        append(next_, y_, distance)
    next_ = y_ - 1
    if next_ >= 0:
        append(x_, next_, distance)
    next_ = y_ + 1
    if n > next_:
        append(x_, next_, distance)


def append(x_, y_, distance):
    if space[x_][y_] <= size and distances[x_][y_] > distance:
        distances[x_][y_] = distance
        deque_.append((x_, y_))


n = int(stdin.readline())
longest = n * 2 - 1
initial = [[longest] * n for _ in range(n)]
space, deque_, distances = [list(map(int, stdin.readline().split())) for _ in range(n)], None, deepcopy(initial)
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j], deque_, distances[i][j] = 0, deque([(i, j)]), 0
            break
    else:
        continue
    break
size, time, eaten = 2, 0, 0
while True:
    while deque_:
        x, y = deque_.popleft()
        omnidirectional_append(x, y)
    shortest, x, y = longest, None, None
    for i in range(n):
        for j in range(n):
            if distances[i][j] < shortest and size > space[i][j] >= 1:
                shortest, x, y = distances[i][j], i, j
    if shortest >= longest:
        break
    space[x][y], time = 0, distances[x][y] + time
    deque_.append((x, y))
    distances = deepcopy(initial)
    distances[x][y], eaten = 0, eaten + 1
    if size <= eaten:
        size, eaten = size + 1, 0
print(time)

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
