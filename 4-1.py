# 상하좌우
import sys

n = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())

directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
current_x = current_y = 1
for plan in plans:
    direction_x, direction_y = directions[plan]
    next_x = current_x + direction_x
    next_y = current_y + direction_y
    if 1 <= next_x <= n >= next_y >= 1:
        current_x = next_x
        current_y = next_y

print(current_x, current_y)
'''
5
R R R U D D

3 4
'''
