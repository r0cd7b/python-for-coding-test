# 탑승구
from sys import stdin


def find_parent(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


g, p = int(stdin.readline()), int(stdin.readline())
parent = [i for i in range(g + 1)]
result = 0
for _ in range(p):
    pass

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
