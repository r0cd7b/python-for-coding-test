# 아기 상어
from sys import stdin
from collections import deque
from copy import deepcopy

n = int(stdin.readline())
initial_visits = [[False] * n for _ in range(n)]
spaces, deque_, visits, baby = [], deque(), deepcopy(initial_visits), {"size": 2, "eaten": 0, "time": 0}
for i in range(n):
    spaces.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        if spaces[i][j] == 9:
            deque_.append((i, j, 0))
            visits[i][j] = True
            break
while deque_:
    x, y, time = deque_.popleft()
    eat, next_time = False, time + 1
    for next_x, next_y in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        if not eat and n > next_x >= 0 and n > next_y >= 0 and not visits[next_x][next_y]:
            if baby["size"] > spaces[next_x][next_y] > 0:
                spaces[next_x][next_y], visits, baby["eaten"], baby["time"], eat = 0, deepcopy(initial_visits), baby[
                    "eaten"] + 1, next_time, True
                deque_.clear()
                if baby["size"] <= baby["eaten"]:
                    baby["size"], baby["eaten"] = baby["size"] + 1, 0

                for space in spaces:
                    print(space)
                print(baby, end='\n\n')

            deque_.append((next_x, next_y, next_time))
            visits[next_x][next_y] = True
print(baby["time"])

"""
입력 예시 1
3
0 0 0
0 0 0
0 9 0
출력 예시 1
0

입력 예시 2
3
0 0 1
0 0 0
0 9 0
출력 예시 2
3

입력 예시 3
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
출력 예시 3
14
"""
