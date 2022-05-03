# 어른 상어
from sys import stdin

n, m, k = map(int, stdin.readline().split())
grid = [[int(s) - 1 for s in stdin.readline().split()] for _ in range(n)]
direction = [int(s) - 1 for s in stdin.readline().split()]
priority = [[[int(s) - 1 for s in stdin.readline().split()] for _ in range(4)] for _ in range(m)]

position = {}
smell = {}
for i in range(n):
    for j in range(n):
        if grid[i][j] >= 0:
            position[grid[i][j]] = (i, j)
            # smell[]

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
move = {}
for shark in position:
    for direction_check in priority[shark][direction[shark]]:
        next_x = position[shark][0] + x[direction_check]
        next_y = position[shark][1] + y[direction_check]
        # if 0 <= next_x < n > next_y >= 0 and :

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