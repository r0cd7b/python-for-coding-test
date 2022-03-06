# 플로이드
from sys import stdin
from heapq import heappush, heappop

n, m = int(stdin.readline()), int(stdin.readline())
buses: list = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    buses[a - 1].append((c, b - 1))

minimums = []
for i in range(n):
    heap, costs = [], [0] * n
    for cost, index in buses[i]:
        heappush(heap, (cost, index))
        costs[index] = cost
    while heap:
        cost_current, index_current = heappop(heap)
        for cost_next, index_next in buses[index_current]:
            if i != index_next:
                cost_next += cost_current
                if not costs[index_next] or costs[index_next] > cost_next:
                    heappush(heap, (cost_next, index_next))
                    costs[index_next] = cost_next
    minimums.append(costs)
for minimums in minimums:
    print(minimums)

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
