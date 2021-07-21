# 간단한 다익스트라 알고리즘 소스코드
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

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input()) - 1
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

start_time = time.time()

INF = int(1e9)
visited = [False] * n
distance = [INF] * n


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(n):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in distance:
    if i >= INF:
        print("INFINITY")
    else:
        print(i)

print(f"time: {time.time() - start_time}")
