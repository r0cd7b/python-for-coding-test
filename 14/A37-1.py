# 플로이드
from sys import stdin

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, graph = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    if not graph[a][b] or graph[a][b] > graph:
        graph[a][b] = graph

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b] and a != b:
                cost = graph[a][k] + graph[k][b]
                if not graph[a][b] or graph[a][b] > cost:
                    graph[a][b] = cost

for g1 in graph:
    for g2 in g1:
        print(g2, end=' ')
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
