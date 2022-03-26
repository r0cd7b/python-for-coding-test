# 탑승구
from sys import stdin


def find_parent(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


G, P = int(stdin.readline()), int(stdin.readline())
g, parent = [int(stdin.readline()) for _ in range(P)], [i for i in range(G + 1)]
for i in range(P):
    if not find_parent(parent, g[i]):
        print(i)
        break
    parent[g[i]] = find_parent(parent, parent[g[i]] - 1)
else:
    print(P)

"""
입력 예시 1
4
3
4
1
1
출력 예시 1
2

입력 예시 2
4
6
2
2
3
3
4
4
출력 예시 2
3
"""
