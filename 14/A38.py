# 정확한 순위
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1][b - 1] = True

for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k != j and graph[j][i] and graph[i][k]:
                    graph[j][k] = True
students = 0
for i in range(n):
    for j in range(n):
        if not (i == j or graph[i][j] or graph[j][i]):
            break
    else:
        students += 1

print(students)

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
