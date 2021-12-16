# 인구 이동
from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]

search, moves = deque(), 0
while True:
    visit, move = [[False] * n for _ in range(n)], False
    for r1 in range(n):
        for c1 in range(n):
            if not visit[r1][c1]:
                search.append((r1, c1))
                visit[r1][c1], union, population = True, [], 0
                while search:
                    r2, c2 = search.popleft()
                    union.append((r2, c2))
                    population += a[r2][c2]
                    r3 = r2 - 1
                    if r3 >= 0 and not visit[r3][c2] and l <= abs(a[r2][c2] - a[r3][c2]) <= r:
                        search.append((r3, c2))
                        visit[r3][c2] = True
                    r3 = r2 + 1
                    if r3 < n and not visit[r3][c2] and l <= abs(a[r2][c2] - a[r3][c2]) <= r:
                        search.append((r3, c2))
                        visit[r3][c2] = True
                    c3 = c2 - 1
                    if c3 >= 0 and not visit[r2][c3] and l <= abs(a[r2][c2] - a[r2][c3]) <= r:
                        search.append((r2, c3))
                        visit[r2][c3] = True
                    c3 = c2 + 1
                    if c3 < n and not visit[r2][c3] and l <= abs(a[r2][c2] - a[r2][c3]) <= r:
                        search.append((r2, c3))
                        visit[r2][c3] = True
                if len(union) >= 2:
                    move, population = True, population // len(union)
                    for r2, c2 in union:
                        a[r2][c2] = population
    if move:
        moves += 1
    else:
        break

print(moves)

"""
입력 예시 1
2 20 50
50 30
20 40
출력 예시 1
1

입력 예시 2
2 40 50
50 30
20 40
출력 예시 2
0

입력 예시 3
2 20 50
50 30
30 40
출력 예시 3
1

입력 예시 4
3 5 10
10 15 20
20 30 25
40 22 10
출력 예시 4
2

입력 예시 5
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
출력 예시 5
3
"""
