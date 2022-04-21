# 청소년 상어
from sys import stdin
from copy import deepcopy

fish = [[] for _ in range(16)]
space = [[0] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, stdin.readline().split()))
    for j in range(4):
        twice = j * 2
        number = data[twice] - 1
        fish[number].append(i)
        fish[number].append(j)
        fish[number].append(data[twice + 1] - 1)
        space[i][j] = number

x = [-1, -1, 0, 1, 1, 1, 0, -1]
y = [0, -1, -1, -1, 0, 1, 1, 1]
x_coordinate = 0
y_coordinate = 0

direction = fish[space[0][0]][2]
maximum = space[0][0] + 1
space[0][0] = 16

for i in range(16):
    if space[fish[i][0]][fish[i][1]] == i:
        for j in range(8):
            next_x = fish[i][0] + x[fish[i][2]]
            next_y = fish[i][1] + y[fish[i][2]]
            if 0 <= next_x <= 3 >= next_y >= 0 and space[next_x][next_y] != 16:
                fish[space[next_x][next_y]][0] = fish[i][0]
                fish[space[next_x][next_y]][1] = fish[i][1]
                space[fish[i][0]][fish[i][1]] = space[next_x][next_y]
                fish[i][0] = next_x
                fish[i][1] = next_y
                space[next_x][next_y] = i
                break
            fish[i][2] = (fish[i][2] + 1) % 8

next_x = x_coordinate + x[direction]
next_y = y_coordinate + y[direction]
stack = []
while 0 <= next_x <= 3 >= next_y >= 0:
    if space[next_x][next_y] < 17:
        maximum = max(space[next_x][next_y] + maximum + 1, maximum)
        branched_space = deepcopy(space)
        branched_space[x_coordinate][y_coordinate] = 17
        branched_space[next_x][next_y] = 16
        stack.append((fish[space[next_x][next_y]][2], next_x, next_y, branched_space))
    next_x += x[direction]
    next_y += y[direction]

while stack:
    direction, x_coordinate, y_coordinate, space = stack.pop()

    for i in range(16):
        if space[fish[i][0]][fish[i][1]] == i:
            for j in range(8):
                next_x = fish[i][0] + x[fish[i][2]]
                next_y = fish[i][1] + y[fish[i][2]]
                if 0 <= next_x <= 3 >= next_y >= 0 and space[next_x][next_y] != 16:
                    branched_fish = deepcopy(fish)

                    branched_fish[space[next_x][next_y]][0] = fish[i][0]
                    branched_fish[space[next_x][next_y]][1] = fish[i][1]
                    space[fish[i][0]][fish[i][1]] = space[next_x][next_y]
                    branched_fish[i][0] = next_x
                    branched_fish[i][1] = next_y
                    space[next_x][next_y] = i
                    break
                fish[i][2] = (fish[i][2] + 1) % 8

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
