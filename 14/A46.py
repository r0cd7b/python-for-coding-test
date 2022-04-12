# 아기 상어
from sys import stdin
from collections import deque
from copy import deepcopy


def first_visit(x_, y_):
    visited_ = deepcopy(space)
    visited_[x_][y_] = visited_space
    omnidirectional_append(x_, y_, 0, visited_)
    return visited_


def omnidirectional_append(x_, y_, distance_, visited_):
    next_ = x_ - 1
    if next_ >= 0:
        append(next_, y_, distance_, visited_)
    next_ = x_ + 1
    if n > next_:
        append(next_, y_, distance_, visited_)
    next_ = y_ - 1
    if next_ >= 0:
        append(x_, next_, distance_, visited_)
    next_ = y_ + 1
    if n > next_:
        append(x_, next_, distance_, visited_)


def append(x_, y_, distance_, visited_):
    distance_ += 1
    if size > visited_[x_][y_] >= 1:
        edible.append((distance_, x_, y_))
    if visited_[x_][y_] <= size:
        visited_[x_][y_] = visited_space
        bfs.append((distance_, x_, y_))


n, visited, size = int(stdin.readline()), None, 2
space, visited_space, edible, bfs = [list(map(int, stdin.readline().split())) for _ in range(n)], n ** 2, [], deque()
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            visited = first_visit(i, j)
            break
    else:
        continue
    break
time = eaten = 0
while True:
    while bfs:
        distance, x, y = bfs.popleft()
        omnidirectional_append(x, y, distance, visited)
    if not edible:
        break
    edible.sort()
    distance, x, y = edible[0]
    eaten, space[x][y] = eaten + 1, 0
    if size <= eaten:
        size, eaten = size + 1, 0
    edible.clear()
    time, visited = time + distance, first_visit(x, y)
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
