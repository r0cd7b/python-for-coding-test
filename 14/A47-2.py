# 청소년 상어
from sys import stdin
from copy import deepcopy


def find_fish(_array, index):
    for _i in range(4):
        for _j in range(4):
            if _array[_i][_j][0] == index:
                return _i, _j
    return None


def turn_left(direction):
    return (direction + 1) % 8


def move_all_fishes(now_x, now_y, _array):
    for _i in range(1, 17):
        position = find_fish(_array, _i)
        if position:
            for _j in range(8):
                nx, ny = \
                    position[0] + dx[_array[position[0]][position[1]][1]], \
                    position[1] + dy[_array[position[0]][position[1]][1]]
                if (now_x, now_y) != (nx, ny) and 0 <= nx <= 3 >= ny >= 0:
                    _array[position[0]][position[1]], _array[nx][ny] = _array[nx][ny], _array[position[0]][position[1]]
                    break
                _array[position[0]][position[1]][1] = turn_left(_array[position[0]][position[1]][1])


def get_possible_positions(now_x, now_y, _array):
    direction, positions = _array[now_x][now_y][1], []
    for _i in range(4):
        now_x, now_y = now_x + dx[direction], now_y + dy[direction]
        if 0 <= now_x <= 3 >= now_y >= 0 and _array[now_x][now_y][0] > -1:
            positions.append((now_x, now_y))
    return positions


def dfs(_array, total, now_x, now_y):
    global result
    _array = deepcopy(_array)
    total, _array[now_x][now_y][0] = total + _array[now_x][now_y][0], -1
    move_all_fishes(now_x, now_y, _array)
    positions = get_possible_positions(now_x, now_y, _array)
    if not positions:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(_array, total, next_x, next_y)


array = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, stdin.readline().split()))
    for j in range(4):
        double = j * 2
        array[i].append([data[double], data[double + 1] - 1])
result, dx, dy = 0, [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
dfs(array, 0, 0, 0)
print(result)

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
