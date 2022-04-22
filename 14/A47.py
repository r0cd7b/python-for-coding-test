# 청소년 상어
from copy import deepcopy
from sys import stdin


def move(_fish, _sum):
    for _i in range(16):
        if space[_fish[_i][0]][_fish[_i][1]] == _i:
            for _j in range(8):
                next_x, next_y = _fish[_i][0] + x[_fish[_i][2]], _fish[_i][1] + y[_fish[_i][2]]
                if 0 <= next_x <= 3 >= next_y >= 0 and space[next_x][next_y] != 16:
                    if space[next_x][next_y] <= 15:
                        _fish[space[next_x][next_y]][0], _fish[space[next_x][next_y]][1] = _fish[_i][0], _fish[_i][1]
                    space[_fish[_i][0]][_fish[_i][1]], space[next_x][next_y], _fish[_i][0], _fish[_i][1] = \
                        space[next_x][next_y], _i, next_x, next_y
                    break
                _fish[_i][2] = (_fish[_i][2] + 1) % 8
    next_x, next_y = shark_x + x[direction], shark_y + y[direction]
    while 0 <= next_x <= 3 >= next_y >= 0:
        if space[next_x][next_y] <= 15:
            branched_space = deepcopy(space)
            branched_space[next_x][next_y], branched_space[shark_x][shark_y], numbers = \
                16, 17, _sum + space[next_x][next_y] + 1
            stack.append((_fish, _fish[space[next_x][next_y]][2], next_x, next_y, branched_space, numbers))
        next_x, next_y = next_x + x[direction], next_y + y[direction]


space, fish = [[0] * 4 for _ in range(4)], [[] for _ in range(16)]
for i in range(4):
    data = list(map(int, stdin.readline().split()))
    for j in range(4):
        twice = j * 2
        number = data[twice] - 1
        space[i][j] = number
        fish[number].append(i)
        fish[number].append(j)
        fish[number].append(data[twice + 1] - 1)
direction, maximum, space[0][0], x, y, shark_x, shark_y, stack = \
    fish[space[0][0]][2], space[0][0] + 1, 16, [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1], 0, 0, []
move(fish, maximum)
while stack:
    fish, direction, shark_x, shark_y, space, sum_ = stack.pop()
    branched_fish, maximum = deepcopy(fish), max(maximum, sum_)
    move(branched_fish, sum_)
print(maximum)

"""
입력 예시 1
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
출력 예시 1
33

입력 예시 2
16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4
출력 예시 2
43

입력 예시 3
12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2
출력 예시 3
76
"""
