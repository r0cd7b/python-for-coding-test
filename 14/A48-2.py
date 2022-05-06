# 어른 상어
from sys import stdin


def update_smell():
    for _x in range(N):
        for _y in range(N):
            if smell[_x][_y][1] >= 1:
                smell[_x][_y][1] -= 1
            if array[_x][_y] >= 0:
                smell[_x][_y][0] = array[_x][_y]
                smell[_x][_y][1] = K


def move():
    new_array = [[-1] * N for _ in range(N)]
    for _x in range(N):
        for _y in range(N):
            if array[_x][_y] >= 0:
                for priority in priorities[array[_x][_y]][directions[array[_x][_y]]]:
                    nx = _x + d[priority][0]
                    ny = _y + d[priority][1]
                    if 0 <= nx <= N - 1 >= ny >= 0 and smell[nx][ny][1] < 1:
                        if not (0 <= new_array[nx][ny] <= array[_x][_y]):
                            directions[array[_x][_y]] = priority
                            new_array[nx][ny] = array[_x][_y]
                        break
                else:
                    for priority in priorities[array[_x][_y]][directions[array[_x][_y]]]:
                        nx = _x + d[priority][0]
                        ny = _y + d[priority][1]
                        if 0 <= nx <= N - 1 >= ny >= 0 and array[_x][_y] == smell[nx][ny][0]:
                            directions[array[_x][_y]] = priority
                            new_array[nx][ny] = array[_x][_y]
                            break
    return new_array


N, M, K = map(int, stdin.readline().split())
array = [[int(s) - 1 for s in stdin.readline().split()] for _ in range(N)]
directions = [int(s) - 1 for s in stdin.readline().split()]
priorities = [[[int(s) - 1 for s in stdin.readline().split()] for _ in range(4)] for _ in range(M)]

smell = [[[-1, 0] for _ in range(N)] for _ in range(N)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(1, 1001):
    update_smell()
    array = move()
    for x in range(N):
        for y in range(N):
            if array[x][y] >= 1:
                break
        else:
            continue
        break
    else:
        print(i)
        break
else:
    print(-1)

"""
입력 예시 1
4 2 6
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
4 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
출력 예시 1
26

입력 예시 2
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
출력 예시 2
14
"""
