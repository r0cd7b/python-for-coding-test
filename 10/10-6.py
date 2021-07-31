# 위상 정렬 소스코드
"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
from sys import stdin
from collections import deque

input = stdin.readline
v, e = map(int, input().split())
in_degree = [0] * v
graph = [[] for _ in range(v)]
for _ in range(e):
    a, b = map(int, input().split())
    b -= 1
    graph[a - 1].append(b)
    in_degree[b] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(v):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    for i in result:
        print(i + 1, end=' ')
    print()


topology_sort()
