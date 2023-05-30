# 음료수 얼려 먹기
from sys import stdin


def dfs(n__, m__):
    frame[n__][m__] = '2'
    for vertical, horizontal in vectors:
        next_n, next_m = n__ + vertical, m__ + horizontal
        if n > next_n >= 0 <= next_m < m and frame[next_n][next_m] == '0':
            dfs(next_n, next_m)


size = stdin.readline().split()
n, m = int(size[0]), int(size[1])
frame = [[shape for shape in stdin.readline().strip()] for _ in range(n)]

vectors, creams = ((-1, 0), (1, 0), (0, -1), (0, 1)), 0
for n_ in range(n):
    for m_ in range(m):
        if frame[n_][m_] == '0':
            dfs(n_, m_)
            creams += 1

print(creams)
"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

8
"""
