# 화성 탐사
from sys import stdin
from heapq import heapify, heappop, heappush

INF, minimums = 125 ** 2 * 9 + 1, []
for _ in range(int(stdin.readline())):
    space = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
    costs: list = [[INF] * len(space) for _ in range(len(space))]
    costs[0][0], costs[0][1], costs[1][0] = space[0][0], space[0][0] + space[0][1], space[0][0] + space[1][0]
    heap = [(costs[0][1], 0, 1), (costs[1][0], 1, 0)]
    heapify(heap)
    while heap:
        cost, y, x = heappop(heap)
        for next_y, next_x in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
            if 0 <= next_y < len(space) and 0 <= next_x < len(space):
                transit = cost + space[next_y][next_x]
                if costs[next_y][next_x] > transit:
                    heappush(heap, (transit, next_y, next_x))
                    costs[next_y][next_x] = transit
    minimums.append(costs[-1][-1])
for minimum in minimums:
    print(minimum)

"""
입력 예시
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
출력 예시
20
19
36
"""
