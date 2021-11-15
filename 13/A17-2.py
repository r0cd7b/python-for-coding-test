# 경쟁적 전염
from sys import stdin
from collections import deque

(n, k), graph, data = map(int, stdin.readline().split()), [], []

for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q, (target_s, target_x, target_y) = deque(data), map(int, stdin.readline().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

'''
입력 예시 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2
출력 예시 1
3

입력 예시 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2
출력 예시 2
0
'''
