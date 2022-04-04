# 최종 순위
from sys import stdin
from collections import deque

results = []
for _ in range(int(stdin.readline())):
    n, t = int(stdin.readline()), [int(s) - 1 for s in stdin.readline().split()]

    entries = [0] * n
    for i in range(n):
        entries[t[i]] = i

    graph = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[t[i]][t[j]] = True

    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        a, b = a - 1, b - 1
        entries[a], entries[b], graph[a][b], graph[b][a] = entries[a] - 1, entries[b] + 1, True, False

    zeros, queue, rank = 0, deque(), ""
    for i in range(n):
        if not entries[i]:
            zeros += 1
            queue.append(i)

    if zeros > 1:
        results.append("?")
        continue

    while queue:
        now, zeros = queue.pop(), 0
        for i in range(n):
            if graph[now][i]:
                entries[i] -= 1
                if not entries[i]:
                    zeros += 1
                    queue.append(i)
        if zeros > 1:
            results.append("?")
            break
        rank += f"{now + 1} "
    else:
        if entries.count(0) < n:
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
