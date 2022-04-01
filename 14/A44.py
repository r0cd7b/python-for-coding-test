# 행성 터널
from sys import stdin


def find_parent(x_):
    while parent[x_] != parent[parent[x_]]:
        parent[x_] = parent[parent[x_]]
    return parent[x_]


n, planets = int(stdin.readline()), []
for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    planets.append((i, x, y, z))
tunnels = []
for i in range(1, 4):
    planets.sort(key=lambda p: p[i])
    for j in range(n - 1):
        next_ = j + 1
        tunnels.append((abs(planets[j][i] - planets[next_][i]), planets[j][0], planets[next_][0]))
parent, minimum = [i for i in range(n)], 0
for cost, a, b in sorted(tunnels):
    if find_parent(a) != find_parent(b):
        minimum, parent[parent[b]] = minimum + cost, parent[a]
print(minimum)

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
