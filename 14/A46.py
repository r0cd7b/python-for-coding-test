# 아기 상어
from sys import stdin
from copy import deepcopy
from heapq import heappush, heappop


def visit_next(distance, x, y):
    visit[x][y], next_ = True, x - 1
    if next_ >= 0:
        push(distance, next_, y)
    next_ = x + 1
    if n > next_:
        push(distance, next_, y)
    next_ = y - 1
    if next_ >= 0:
        push(distance, x, next_)
    next_ = y + 1
    if n > next_:
        push(distance, x, next_)


def push(distance, x, y):
    if space[x][y] <= size and not visit[x][y]:
        heappush(heap, (distance + 1, x, y))


n = int(stdin.readline())
initial = [[False] * n for _ in range(n)]
space, visit, size, heap = [list(map(int, stdin.readline().split())) for _ in range(n)], deepcopy(initial), 2, []
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            visit_next(0, i, j)
            break
    else:
        continue
    break
eaten, time = 0, 0
while heap:
    distance_, x_, y_ = heappop(heap)
    if size > space[x_][y_] >= 1:
        space[x_][y_], visit, eaten, time, distance_ = 0, deepcopy(initial), eaten + 1, time + distance_, 0
        heap.clear()
        if size <= eaten:
            size, eaten = size + 1, 0
    visit_next(distance_, x_, y_)
print(time)

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
