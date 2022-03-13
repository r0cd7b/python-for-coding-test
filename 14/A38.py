# 정확한 순위
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = True

for k in range(n):
    for a in range(n):
        if k != a:
            for b in range(n):
                if k != b != a and graph[a][k] and graph[k][b]:
                    graph[a][b] = True
result = 0
for i in range(n):
    for j in range(n):
        if not (i == j or graph[i][j] or graph[j][i]):
            break
    else:
        result += 1

print(result)

"""
입력 예시
6 6
1 5
3 4
4 2
4 6
5 2
5 4
출력 예시
1
"""
