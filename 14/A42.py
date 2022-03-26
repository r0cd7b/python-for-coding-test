# 탑승구
from sys import stdin


def find_parent(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


g, p = int(stdin.readline()), int(stdin.readline())
gates, result, parent = [int(stdin.readline()) for _ in range(p)], 0, [i for i in range(g + 1)]
while p > result and find_parent(gates[result]):
    parent[gates[result]], result = find_parent(parent[gates[result]] - 1), result + 1
print(result)

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
