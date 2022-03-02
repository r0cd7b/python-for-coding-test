# 플로이드
from sys import stdin
from heapq import heappush, heappop

n, m = int(stdin.readline()), int(stdin.readline())
buses = [[1e5] * i + [0] + [1e5] * (n - i - 1) for i in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    if buses[a][b] > c:
        buses[a][b] = c
print(buses)

for i in range(n):
    for j in range(n):
        if buses[i][j] >= 2:
            heap = [(0, i)]
            while heap:
                cost, destination = heappop(heap)
                if buses[i][destination] > cost:
                    for k in range(n):
                        cost += buses[destination][k]
                        if buses[destination][k] > cost:
                            buses[destination][k] = cost
                            heappush(heap, (buses[i][k], k))

"""
입력 예시
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
출력 예시
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
"""
