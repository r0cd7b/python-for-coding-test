# 금광
from sys import stdin

t, mines = int(stdin.readline()), []
for _ in range(t):
    (n, m), golds = map(int, stdin.readline().split()), list(map(int, stdin.readline().split()))
    mines.append([golds[i * m:i * m + m] for i in range(n)])

maximum = []
for mine in mines:
    for i in range(1, len(mine[0])):
        for j in range(len(mine)):
            mine[j][i] += max(mine[j - 1][i - 1] if j >= 1 else 0, mine[j][i - 1],
                              mine[j + 1][i - 1] if j < len(mine) - 1 else 0)
    size = mine[0][-1]
    for i in range(1, len(mine)):
        size = max(mine[i][-1], size)
    maximum.append(size)

for size in maximum:
    print(size)

"""
입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
