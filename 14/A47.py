# 청소년 상어
from sys import stdin

space, shark_fish = [[0] * 4 for _ in range(4)], [[0, 0, 0] for _ in range(17)]
for i in range(4):
    line = list(map(int, stdin.readline().split()))
    for j in range(4):
        space[i][j], shark_fish[line[j * 2]][0], shark_fish[line[j * 2]][1], shark_fish[line[j * 2]][2] \
            = line[j * 2], i, j, line[j * 2 + 1]

maximum = space[0][0]
shark_fish[0][2] = shark_fish[space[0][0]][2]
shark_fish[space[0][0]][2] = 0
space[0][0] = 0

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
