# 행성 터널
from sys import stdin

n, planets, edges, result = int(stdin.readline()), [], [], 0
for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    planets.append((i, x, y, z))
for i in range(1, 4):
    planets.sort(key=lambda p: p[i])
    for j in range(n - 1):
        edges.append((planets[j + 1][i] - planets[j][i], planets[j][0], planets[j + 1][0]))
parent = [i for i in range(n)]
for cost, a, b in sorted(edges):
    while parent[a] != parent[parent[a]]:
        parent[a] = parent[parent[a]]
    while parent[b] != parent[parent[b]]:
        parent[b] = parent[parent[b]]
    if parent[a] != parent[b]:
        result, parent[parent[b]] = result + cost, parent[a]
print(result)

"""
입력 예시
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
출력 예시
4
"""
