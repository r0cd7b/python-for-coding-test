# 플로이드
from sys import stdin
from heapq import heappush, heappop

n, m = int(stdin.readline()), int(stdin.readline())
buses = [[1e5] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    buses[a - 1][b - 1] = c

minimum = []
for i in range(n):
    minimum.append([])
    for j in range(n):
        if i == j:
            minimum[i].append(0)
            continue

        queue, visit = [], [False] * n
        visit[i] = True
        for cost in buses[i]:
            heappush(queue, (cost, j))
        while queue:
            cost, destination = heappop(queue)

print(buses)

"""
입력 예시
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
출력 예시
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
"""
