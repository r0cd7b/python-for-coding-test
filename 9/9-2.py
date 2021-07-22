# 개선된 다익스트라 알고리즘 소스코드
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
import sys
import time
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input()) - 1
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

start_time = time.time()

INF = int(1e9)
distance = [INF] * n


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] >= dist:
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in distance:
    if i >= INF:
        print("INFINITY")
    else:
        print(i)

print(f"time: {time.time() - start_time}")
