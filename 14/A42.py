# 탑승구
from sys import stdin


def find_parent(parent_, x):
    while parent_[x] != parent_[parent_[x]]:
        parent_[x] = parent_[parent_[x]]


G, P = int(stdin.readline()), int(stdin.readline())
g, parent = [int(stdin.readline()) for _ in range(P)], [i for i in range(G + 1)]
for i in range(P):
    find_parent(parent, g[i])
    if not parent[g[i]]:
        print(i)
        break
    previous = parent[g[i]] - 1
    find_parent(parent, previous)
    parent[g[i]] = parent[previous]
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
