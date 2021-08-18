# 커리큘럼
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from sys import stdin
from collections import deque
import copy

v = int(stdin.readline())
time = [0] * v
in_degree = [0] * v
graph = [[] for _ in range(v)]
for i in range(v):
    data = list(map(int, stdin.readline().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        in_degree[i] += 1
        graph[x - 1].append(i)


def topology_sort(in_degree):
    q = deque()
    for i in range(v):
        if in_degree[i] == 0:
            q.append(i)
    result = copy.deepcopy(time)
    while q:
        now = q.popleft()
        for i in graph[now]:
            in_degree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if in_degree[i] == 0:
                q.append(i)
    for i in range(v):
        print(result[i])


topology_sort(in_degree)
