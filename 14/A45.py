# 최종 순위
from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    graph, t = [[False] * n for _ in range(n)], list(map(int, stdin.readline().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[t[i]][t[j]] = True
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        a, b = a - 1, b - 1
        graph[a][b], graph[b][a] = True, False
    degree = []

"""
입력 예시
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
출력 예시
5 3 2 4 1
2 3 1
IMPOSSIBLE
"""
