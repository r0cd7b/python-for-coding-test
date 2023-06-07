# 미로 탈출
from collections import deque
from sys import stdin

size = stdin.readline().split()
n, m = int(size[0]), int(size[1])
maze = [[int(square) - 1 for square in stdin.readline().strip()] for _ in range(n)]

maze[0][0], queue, vectors, exit_n, exit_m = 1, deque([(0, 0)]), ((-1, 0), (1, 0), (0, -1), (0, 1)), n - 1, m - 1
while queue:
    current_n, current_m = queue.popleft()
    for n_move, m_move in vectors:
        next_n, next_m, next_moves = current_n + n_move, current_m + m_move, maze[current_n][current_m] + 1
        if next_n == exit_n and next_m == exit_m:
            print(next_moves)
            break
        if n > next_n >= 0 <= next_m < m and not maze[next_n][next_m]:
            maze[next_n][next_m] = next_moves
            queue.append((next_n, next_m))
    else:
        continue
    break
"""
5 6
101010
111111
000001
111111
111111

10
"""
