# 플로이드
from sys import stdin
from heapq import heappush, heappop

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[0] * n for i in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    if not graph[a][b] or graph[a][b] > c:
        graph[a][b] = c

minimums = []
for i in range(n):
    heap, costs = [], [0] * n
    for j in range(n):
        if graph[i][j] and i != j:
            heappush(heap, (graph[i][j], j))
            costs[j] = graph[i][j]
    while heap:
        cost_current, index = heappop(heap)
        for j in range(n):
            if graph[index][j] and i != j and index != j:
                cost_next = graph[index][j] + cost_current
                if not costs[j] or costs[j] > cost_next:
                    heappush(heap, (cost_next, j))
                    costs[j] = cost_next
    minimums.append(costs)

for m1 in minimums:
    for m2 in m1:
        print(m2, end=' ')
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
