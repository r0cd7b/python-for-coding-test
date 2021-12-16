# 인구 이동
from sys import stdin


def d(row, co):
    v[row][co] = True
    u.append((row, co))
    global p, l, r
    p += a[row][co]
    coo = row - 1
    if coo >= 0 and not v[coo][co] and l <= abs(a[row][co] - a[coo][co]) <= r:
        d(coo, co)
    coo = row + 1
    if coo < n and not v[coo][co] and l <= abs(a[row][co] - a[coo][co]) <= r:
        d(coo, co)
    coo = co - 1
    if coo >= 0 and not v[row][coo] and l <= abs(a[row][co] - a[row][coo]) <= r:
        d(row, coo)
    coo = co + 1
    if coo < n and not v[row][coo] and l <= abs(a[row][co] - a[row][coo]) <= r:
        d(row, coo)


n, l, r = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]

t = 0
while True:
    v, m = [[False] * n for _ in range(n)], False
    for ro in range(n):
        for c in range(n):
            u, p = [], 0
            d(ro, c)
            if len(u) >= 2:
                p //= len(u)
                for row_, col in u:
                    if p != a[row_][col]:
                        a[row_][col] = p
                        m = True
    if m:
        t += 1
    else:
        break

print(t)

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
