# 특정 거리의 도시 찾기
from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b - 1)

visited = [False] * n

x -= 1
queue = deque([(x, 0)])
numbers = []
visited[x] = True
while queue:
    city = queue.popleft()
    if city[1] == k:
        numbers.append(city[0])

    for next in graph[city[0]]:
        if not visited[next]:
            queue.append((next, city[1] + 1))
            visited[next] = True

if numbers:
    numbers.sort()
    for number in numbers:
        print(number + 1)
else:
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
