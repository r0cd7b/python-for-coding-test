# 어른 상어
from sys import stdin


def move(_x, _y):
    grids[_x][_y].append(shark)
    sharks[shark][2] = _x
    sharks[shark][3] = _y


N, M, K = map(int, stdin.readline().split())

grids: list[list[list[int]]] = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    string = stdin.readline().split()
    for j in range(N):
        if string[j] != '0':
            grids[i][j].append(int(string[j]))

string = stdin.readline().split()
sharks = {i + 1: [int(string[i]) - 1] for i in range(M)}

for i in range(M):
    sharks[i + 1].append(tuple(tuple(int(string) - 1 for string in stdin.readline().split()) for _ in range(4)))

for i in range(N):
    for j in range(N):
        if grids[i][j]:
            sharks[grids[i][j][0]].append(i)
            sharks[grids[i][j][0]].append(j)

vectors = ((-1, 1, 0, 0), (0, 0, -1, 1))
for shark in sharks:
    go = []

    for direction in sharks[shark][1][sharks[shark][0]]:
        next_ = (sharks[shark][2] + vectors[0][direction], sharks[shark][3] + vectors[1][direction])
        if 0 <= next_[0] < N > next_[1] >= 0:
            go.append((next_[0], next_[1]))

    for x, y in go:
        if not grids[x][y]:
            move(x, y)
            break
    else:
        for x, y in go:
            if grids[x][y][0] == shark:
                move(x, y)
                break

    for i in range(N):
        for j in range(N):
            if len(grids[i][j]) > 1:
                index = 0
                for k in range(1, len(grids[i][j])):
                    if grids[i][j][index] > grids[i][j][k]:
                        index = k
                if index > 0:
                    grids[i][j][index], grids[i][j][0] = grids[i][j][0], grids[i][j][index]
                for k in range(-1, -len(grids[i][j]), -1):
                    del shark[grids[i][j][k]]
                    del grids[i][j][k]

for g in grids:
    print(g)
print(sharks)

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
"""
