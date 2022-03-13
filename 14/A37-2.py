# 플로이드
from sys import stdin

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[9900001] * i + [0] + [9900001] * (n - i - 1) for i in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(n):
    for a in range(n):
        if a != k:
            for b in range(n):
                if k != b != a:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for g1 in graph:
    for g2 in g1:
        if g2 > 9900000:
            print(0, end=' ')
        else:
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
