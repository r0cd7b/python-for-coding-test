# 아기 상어
from sys import stdin
from copy import deepcopy


def first_append(x_, y_):
    visited_ = deepcopy(space)
    omnidirectional_append(x_, y_, visited_, 0)
    return visited_


def omnidirectional_append(x_, y_, visited_, distance_):
    next_ = x_ - 1
    if next_ >= 0:
        append(visited_, next_, y_, distance_)
    next_ = x_ + 1
    if n > next_:
        append(visited_, next_, y_, distance_)
    next_ = y_ - 1
    if next_ >= 0:
        append(visited_, x_, next_, distance_)
    next_ = y_ + 1
    if n > next_:
        append(visited_, x_, next_, distance_)


def append(visited_, x_, y_, distance_):
    if size >= visited_[x_][y_] >= 0:
        visited_[x_][y_] = -1
        go.append((distance_ + 1, x_, y_))


n = int(stdin.readline())
space, visited, size, go = [list(map(int, stdin.readline().split())) for _ in range(n)], None, 2, []
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            visited = first_append(i, j)
            break
    else:
        continue
    break
time = eaten = 0
while True:
    for distance, x, y in go:
        omnidirectional_append(x, y, visited, distance)
    go.sort()
    for distance, x, y in go:
        if size > space[x][y] >= 1:
            space[x][y] = 0
            go.clear()
            visited, time, eaten = first_append(x, y), time + distance, eaten + 1
            if size <= eaten:
                size, eaten = size + 1, 0
            break
    else:
        break
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
