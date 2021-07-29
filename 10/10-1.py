# 기본적인 서로소 집합 알고리즘 소스코드
"""
6 4
1 4
2 3
2 4
5 6
"""
from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, stdin.readline().split())
parent = [0] * v
for i in range(v):
    parent[i] = i
for i in range(e):
    a, b = map(int, stdin.readline().split())
    union_parent(parent, a - 1, b - 1)
print("각 원소가 속한 집합: ", end='')
for i in range(v):
    print(find_parent(parent, i) + 1, end=' ')
print("\n부모 테이블: ", end='')
for i in range(v):
    print(parent[i] + 1, end=' ')
