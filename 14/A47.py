# 청소년 상어
from sys import stdin
from copy import deepcopy


def append(_x, _y):
    _x, _y = _x + x_axis[fish[0][2]], _y + y_axis[fish[0][2]]
    while 0 <= _x <= 3 >= _y >= 0:
        stack.append((x, y))
        _x, _y = _x + x_axis[fish[0][2]], _y + y_axis[fish[0][2]]


fish, space = [[] for _ in range(17)], [[17] * 4 for _ in range(4)]
for i in range(4):
    stdin = list(map(int, stdin.readline().split()))
    for j in range(4):
        j_2 = j * 2
        fish[stdin[j_2]].append(i)
        fish[stdin[j_2]].append(j)
        fish[stdin[j_2]].append(stdin[j_2 + 1] - 1)
        space[i][j] = stdin[j_2]

fish[0].append(0)
fish[0].append(0)
fish[0].append(fish[space[0][0]][2])
fish[space[0][0]].clear()
fish[0].append(space[0][0])
space[0][0] = 0

x_axis, y_axis = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(1, 17):
    if fish[i]:
        for j in range(8):
            next_x, next_y = fish[i][0] + x_axis[fish[i][2]], fish[i][1] + y_axis[fish[i][2]]
            if space[next_x][next_y] and 0 <= next_x <= 3 >= next_y >= 0:
                fish[space[next_x][next_y]][0], \
                fish[space[next_x][next_y]][1], \
                space[fish[i][0]][fish[i][1]], \
                fish[i][0], \
                fish[i][1], \
                space[next_x][next_y] = \
                    fish[i][0], fish[i][1], space[next_x][next_y], next_x, next_y, i
                break
            fish[i][2] = (fish[i][2] + 1) % 8

stack = []
append(fish[0][0], fish[0][1])
while stack:
    x, y = stack.pop()
    append(x, y)

print()
for s in space:
    print(s)
print(fish)

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
