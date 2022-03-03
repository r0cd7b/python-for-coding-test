# 플로이드
from sys import stdin
from heapq import heappush, heappop

n, m = int(stdin.readline()), int(stdin.readline())
costs = [[1e5] * i + [0] + [1e5] * (n - i - 1) for i in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    if costs[a][b] > c:
        costs[a][b] = c

for i in range(n):
    heap = []
    for j in range(n):
        heappush(heap, (costs[i][j], j))
    while heap:
        cost, destination = heappop(heap)
        for j in range(n):
            via = cost + costs[destination][j]
            if costs[i][j] > via:
                costs[i][j] = via
                heappush(heap, (costs[i][j], j))

for costs in costs:
    for cost in costs:
        print(cost, end=' ')
    print()

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
