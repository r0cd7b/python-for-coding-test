# 청소년 상어
from sys import stdin

shark_fish, space = [[] for _ in range(17)], [[17] * 4 for _ in range(4)]
for i in range(4):
    line = list(map(int, stdin.readline().split()))
    for j in range(4):
        twice = j * 2
        shark_fish[line[twice]].append(i)
        shark_fish[line[twice]].append(j)
        shark_fish[line[twice]].append(line[twice + 1] - 1)
        space[i][j] = line[twice]
shark_fish[0].append(0)
shark_fish[0].append(0)
shark_fish[0].append(shark_fish[space[0][0]][0])
shark_fish[space[0][0]].clear()
x, y, maximum, space[0][0] = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1], space[0][0], 0

for i in range(1, 17):
    if shark_fish[i]:
        for j in range(8):
            next_x = shark_fish[i][0] + x[shark_fish[i][2]]
            next_y = shark_fish[i][1] + y[shark_fish[i][2]]
            if (shark_fish[0][0], shark_fish[0][1]) != (next_x, next_y) and 0 <= next_x <= 3 >= next_y >= 0:
                shark_fish[space[next_x][next_y]][0], \
                shark_fish[space[next_x][next_y]][1], \
                space[shark_fish[i][0]][shark_fish[i][1]], \
                shark_fish[i][0], \
                shark_fish[i][1], \
                space[next_x][next_y] = \
                    shark_fish[i][0], shark_fish[i][1], space[next_x][next_y], next_x, next_y, i
                break
            shark_fish[i][2] = (shark_fish[i][2] + 1) % 8

print()
for s in space:
    print(s)
print(shark_fish)

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
