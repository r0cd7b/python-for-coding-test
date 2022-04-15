# 아기 상어
from sys import stdin
from collections import deque


def bfs():
    q, dist = deque([(now_x, now_y)]), [[-1] * n for _ in range(n)]
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for _i in range(4):
            nx, ny = x + [-1, 0, 1, 0][_i], y + [0, 1, 0, -1][_i]
            if 0 <= nx < n > ny >= 0 > dist[nx][ny] and array[nx][ny] <= now_size:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    return dist


def find(dist):
    inf = n ** 2
    min_dist, x, y = inf, 0, 0
    for _i in range(n):
        for _j in range(n):
            if now_size > array[_i][_j] >= 1 <= dist[_i][_j] < min_dist:
                min_dist, x, y = dist[_i][_j], _i, _j
    if min_dist < inf:
        return min_dist, x, y
    return None


n = int(stdin.readline())
array, now_x, now_y = [list(map(int, stdin.readline().split())) for _ in range(n)], 0, 0
for i in range(n):
    for j in range(n):
        if array[i][j] >= 9:
            array[i][j], now_x, now_y = 0, i, j
now_size, ate, result = 2, 0, 0
while True:
    value = find(bfs())
    if value is None:
        break
    array[value[1]][value[2]], now_x, now_y, ate, result = 0, value[1], value[2], ate + 1, result + value[0]
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
