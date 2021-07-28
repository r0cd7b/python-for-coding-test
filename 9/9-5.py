# 전보
"""
3 2 1
1 2 4
1 3 2
"""
import sys
import time
import heapq

input = sys.stdin.readline
n, m, start = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x - 1].append((y - 1, z))

start_time = time.time()

INF = int(1e9)
distance = [INF] * n


def dijkstra(distance, start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] >= dist:
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


dijkstra(distance, start - 1)
count = 0
max_distance = 0
for d in distance:
    if d < INF:
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)

print(f"time: {time.time() - start_time}")
