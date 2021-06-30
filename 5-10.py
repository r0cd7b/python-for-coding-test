"""
음료수 얼려 먹기
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
import time

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
        graph[x][y] = -1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)

print(f"time: {time.time() - start_time}")
