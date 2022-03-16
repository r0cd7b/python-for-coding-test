# 화성 탐사
from sys import stdin
from heapq import heappop, heappush

costs = []
for _ in range(int(stdin.readline())):
    graph = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
    distance, q = [[140625] * len(graph) for _ in range(len(graph))], [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]
    while q:
        dist, x, y = heappop(q)
        for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                cost = graph[nx][ny] + dist
                if distance[nx][ny] > cost:
                    heappush(q, (cost, nx, ny))
                    distance[nx][ny] = cost
    costs.append(distance[-1][-1])
for cost in costs:
    print(cost)

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
