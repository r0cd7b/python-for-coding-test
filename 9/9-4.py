# 미래 도시
"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
import sys
import time

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
x, k = map(int, input().split())
print(x, k)
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
print(x, k)

start_time = time.time()

print(f"time: {time.time() - start_time}")
