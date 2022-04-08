# 아기 상어
from sys import stdin
from copy import deepcopy
from heapq import heappop, heappush

n = int(stdin.readline())
space, heap, initial = [list(map(int, stdin.readline().split())) for _ in range(n)], [], [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            space[i][j] = 0
            heap.append((0, i, j))
            break
    else:
        continue
    break
visit, size, eaten, time = deepcopy(initial), 2, 0, 0
while heap:
    distance, x, y = heappop(heap)
    visit[x][y] = True
    for next_x, next_y in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if n > next_x >= 0 and n > next_y >= 0 and space[x][y] <= size and not visit[next_x][next_y]:
            added = distance + 1
            if size > space[next_x][next_y] >= 1:
                space[next_x][next_y], heap, visit, eaten, time = \
                    0, [(0, next_x, next_y)], deepcopy(initial), eaten + 1, time + added
                if size <= eaten:
                    size, eaten = size + 1, 0
                break
            heappush(heap, (added, next_x, next_y))
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
