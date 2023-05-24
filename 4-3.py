# 왕실의 나이트
import sys
from time import perf_counter

coordinate = sys.stdin.readline()
start = perf_counter()

current_column = ord(coordinate[0]) - ord('a') + 1
current_row = int(coordinate[1])
cases = 0
for column_movement, row_movement in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)):
    next_column = current_column + column_movement
    next_row = current_row + row_movement
    if 1 <= next_column <= 8 >= next_row >= 1:
        cases += 1

print(perf_counter() - start)
print(cases)
'''
a1

2
'''
