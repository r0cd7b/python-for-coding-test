# 아기 상어
from sys import stdin
from collections import deque


def bfs():
    array[now_x][now_y], dist = 0, [[inf] * n for _ in range(n)]
    dist[now_x][now_y], q = 0, deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if n > nx >= 0 <= ny < n and array[nx][ny] <= now_size and inf <= dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist


def find(dist):
    min_dist, x, y = inf, None, None
    for _i in range(n):
        for _j in range(n):
            if now_size > array[_i][_j] >= 1 and dist[_i][_j] < min_dist:
                min_dist, x, y = dist[_i][_j], _i, _j
    return min_dist, x, y


n = int(stdin.readline())
array, now_x, now_y = [list(map(int, stdin.readline().split())) for _ in range(n)], 0, 0
for i in range(n):
    for j in range(n):
        if array[i][j] >= 9:
            array[i][j], now_x, now_y = 0, i, j
inf, now_size, ate, result = n ** 2, 2, 0, 0
while True:
    value, now_x, now_y = find(bfs())
    if inf <= value:
        break
    ate, result = ate + 1, result + value
    if now_size <= ate:
        now_size, ate = now_size + 1, 0
print(result)

"""
입력 예시 1
3
0 0 0
0 0 0
0 9 0
출력 예시 1
0

입력 예시 2
3
0 0 1
0 0 0
0 9 0
출력 예시 2
3

입력 예시 3
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
출력 예시 3
14
"""
