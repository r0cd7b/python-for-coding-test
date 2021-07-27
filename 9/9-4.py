# 미래 도시
"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
"""
import sys
import time

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a][b], graph[b][a] = 1, 1
x, k = map(int, input().split())

start_time = time.time()

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0
for c in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
k -= 1
distance = graph[0][k] + graph[k][x - 1]
print(-1 if distance >= INF else distance)

print(f"time: {time.time() - start_time}")
