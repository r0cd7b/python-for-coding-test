# 특정 거리의 도시 찾기
from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b - 1)

x -= 1
queue = deque([x])
distances = [0] * n
while queue:
    city = queue.popleft()
    for next in graph[city]:
        if distances[next] == 0:
            queue.append(next)
            distances[next] = distances[city] + 1

existence = False
for i in range(len(distances)):
    if distances[i] == k:
        existence = True
        print(i + 1)
if not existence:
    print(-1)

'''
입력 예시 1
4 4 2 1
1 2
1 3
2 3
2 4
출력 예시 1
4

입력 예시 2
4 3 2 1
1 2
1 3
1 4
출력 예시 2
-1

입력 예시 3
4 4 1 1
1 2
1 3
2 3
2 4
출력 예시 3
2
3
'''
