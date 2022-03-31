# 행성 터널
from sys import stdin


def find_parent(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


n = int(stdin.readline())
planets = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
tunnels, parent, minimum = sorted([(min(abs(planets[i][0] - planets[j][0]), abs(planets[i][1] - planets[j][1]),
                                        abs(planets[i][2] - planets[j][2])), i, j) for i in range(n - 1) for j in
                                   range(i + 1, n)]), [i for i in range(n)], 0
for cost, a, b in tunnels:
    if find_parent(a) != find_parent(b):
        parent[parent[b]], minimum = parent[a], minimum + cost
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
