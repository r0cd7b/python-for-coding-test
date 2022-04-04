# 최종 순위
from sys import stdin
from collections import deque

results = []
for _ in range(int(stdin.readline())):
    n, data = int(stdin.readline()), [int(s) - 1 for s in stdin.readline().split()]

    degree, graph = [0] * n, [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            degree[data[j]], graph[data[i]][data[j]] = degree[data[j]] + 1, True

    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        a, b = a - 1, b - 1
        x = 1 if graph[a][b] else -1
        degree[a], degree[b], graph[a][b], graph[b][a] = degree[a] + x, degree[b] - x, not graph[a][b], graph[a][b]

    zeros, queue, rank = 0, deque(), ""
    for i in range(n):
        if not degree[i]:
            zeros += 1
            queue.append(i)

    if zeros > 1:
        results.append("?")
        continue

    while queue:
        now, zeros = queue.pop(), 0
        for i in range(n):
            if graph[now][i]:
                degree[i] -= 1
                if not degree[i]:
                    zeros += 1
                    queue.append(i)
        if zeros > 1:
            results.append("?")
            break
        rank += f"{now + 1} "
    else:
        if degree.count(0) < n:
            results.append("IMPOSSIBLE")
        else:
            results.append(rank)

for result in results:
    print(result)

"""
입력 예시
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
출력 예시
5 3 2 4 1
2 3 1
IMPOSSIBLE
"""
