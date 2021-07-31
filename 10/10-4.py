# 서로소 집합을 활용한 사이클 판별 소스코드
"""
3 3
1 2
1 3
2 3
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
for i in range(v):
    parent[i] = i
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
