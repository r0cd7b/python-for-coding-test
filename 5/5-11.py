"""
미로 탈출
5 6
101010
111111
000001
111111
111111
"""
import time
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == 0 and ny == 0:
                continue
            if graph[nx][ny] != 1:
                continue
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    return graph[-1][-1]


print(bfs(0, 0))

print(f"time: {time.time() - start_time}")
