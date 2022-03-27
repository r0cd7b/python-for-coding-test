# 어두운 길
from sys import stdin


def find_parent(x_):
    while parent[x_] != parent[parent[x_]]:
        parent[x_] = parent[parent[x_]]
    return parent[x_]


(n, m), edges, result = map(int, stdin.readline().split()), [], 0
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    edges.append((z, x, y))
    result += z
parent = [i for i in range(n)]
for cost, a, b in sorted(edges):
    if find_parent(a) != find_parent(b):
        result, parent[parent[b]] = result - cost, parent[a]
print(result)

"""
입력 예시
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
출력 예시
51
"""
