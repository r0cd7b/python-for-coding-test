# 크루스칼 알고리즘 소스코드
"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = stdin.readline
v, e = map(int, input().split())
parent = [0] * v
edges = []
result = 0
for i in range(v):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a - 1, b - 1))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
