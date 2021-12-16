# 인구 이동
from sys import stdin
from collections import deque


def process(x, y):
    union[x][y], q, summary, united = True, deque([(x, y)]), graph[x][y], [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not union[nx][ny] and l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                union[nx][ny], summary = True, graph[nx][ny] + summary
                q.append((nx, ny))
                united.append((nx, ny))
    if len(united) >= 2:
        summary //= len(united)
        for i, j in united:
            graph[i][j] = summary
        return True
    return False


n, l, r = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

dx, dy, total_count = [-1, 0, 1, 0], [0, -1, 0, 1], 0
while True:
    union, movement = [[False] * n for _ in range(n)], False
    for i in range(n):
        for j in range(n):
            if not union[i][j] and process(i, j):
                movement = True
    if not movement:
        break
    total_count += 1

print(total_count)

"""
입력 예시 1
2 20 50
50 30
20 40
출력 예시 1
1

입력 예시 2
2 40 50
50 30
20 40
출력 예시 2
0

입력 예시 3
2 20 50
50 30
30 40
출력 예시 3
1

입력 예시 4
3 5 10
10 15 20
20 30 25
40 22 10
출력 예시 4
2

입력 예시 5
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
출력 예시 5
3
"""
