# 어른 상어
from sys import stdin


def allocate_shark(_x, _y, _shark):
    grids[_x][_y].append(K)
    grids[_x][_y].append(_shark)
    smells.append((_x, _y))


def move_shark():
    sharks[shark][0] = direction
    sharks[shark][2] = x
    sharks[shark][3] = y


N, M, K = map(int, stdin.readline().split())
grids: list[list[list[int]]] = [[[] for _ in range(N)] for _ in range(N)]
smells = []
for i in range(N):
    string = stdin.readline().split()
    for j in range(N):
        if string[j] != '0':
            allocate_shark(i, j, int(string[j]))
string = stdin.readline().split()
sharks = {i + 1: [int(string[i]) - 1] for i in range(M)}
for i in range(M):
    sharks[i + 1].append(tuple(tuple(int(string) - 1 for string in stdin.readline().split()) for _ in range(4)))

for i in range(N):
    for j in range(N):
        if grids[i][j]:
            sharks[grids[i][j][1]].append(i)
            sharks[grids[i][j][1]].append(j)
vectors = ((-1, 1, 0, 0), (0, 0, -1, 1))

for i in range(3):
    for g in grids:
        print(g)
    print(sharks)
    print(smells)
    print()

    for shark in sharks:
        go = []
        for direction in sharks[shark][1][sharks[shark][0]]:
            next_ = (sharks[shark][2] + vectors[0][direction], sharks[shark][3] + vectors[1][direction])
            if 0 <= next_[0] < N > next_[1] >= 0:
                go.append((direction, next_[0], next_[1]))
        for direction, x, y in go:
            if not grids[x][y]:
                allocate_shark(x, y, shark)
                move_shark()
                break
        else:
            for direction, x, y in go:
                if grids[x][y][1] == shark:
                    grids[x][y][0] = K
                    move_shark()
                    break

    for j in range(N):
        for k in range(N):
            if len(grids[j][k]) > 2:
                index = 1
                for m in range(2, len(grids[j][k])):
                    if grids[j][k][index] > grids[j][k][m]:
                        index = m
                grids[j][k][index], grids[j][k][1] = grids[j][k][1], grids[j][k][index]
                for m in range(2, len(grids[j][k])):
                    del sharks[grids[j][k][m]]
                grids[j][k] = [grids[j][k][0], grids[j][k][index]]

    new_smells = []
    while smells:
        smell = smells.pop()
        if grids[smell[0]][smell[1]][0] > 1:
            grids[smell[0]][smell[1]][0] -= 1
            new_smells.append(smell)
        else:
            grids[smell[0]][smell[1]].clear()
    smells = new_smells

    if len(sharks) < 2:
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
