# 최종 순위
from sys import stdin
from collections import deque

results = []
for _ in range(int(stdin.readline())):
    n, data = int(stdin.readline()), [int(s) - 1 for s in stdin.readline().split()]
    in_degree, graph = [0] * n, [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            in_degree[data[j]], graph[data[i]][data[j]] = in_degree[data[j]] + 1, True
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        a, b = a - 1, b - 1
        one = 1 if graph[a][b] else -1
        in_degree[a], in_degree[b], graph[a][b], graph[b][a] = in_degree[a] + one, in_degree[b] - one, not graph[a][b], \
                                                               graph[a][b]
    q = deque()
    for i in range(n):
        if not in_degree[i]:
            q.append(i)
    result = []
    for _ in range(n):
        if len(q) < 1:
            results.append("IMPOSSIBLE")
            break
        if len(q) > 1:
            results.append("?")
            break
        now = q.pop()
        result.append(str(now + 1))
        for i in range(n):
            if graph[now][i]:
                in_degree[i] -= 1
                if not in_degree[i]:
                    q.append(i)
    else:
        results.append(' '.join(result))
print('\n'.join(results))

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
