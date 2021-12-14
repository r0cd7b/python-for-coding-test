# 인구 이동
from sys import stdin


def dfs(row, column):
    visits[row][column] = True
    union.append((row, column))
    global l, r
    coordinate = row - 1
    if coordinate >= 0 and not visits[coordinate][column] and l <= abs(a[row][column] - a[coordinate][column]) <= r:
        dfs(coordinate, column)
    coordinate = row + 1
    if coordinate < n and not visits[coordinate][column] and l <= abs(a[row][column] - a[coordinate][column]) <= r:
        dfs(coordinate, column)
    coordinate = column - 1
    if coordinate >= 0 and not visits[row][coordinate] and l <= abs(a[row][column] - a[row][coordinate]) <= r:
        dfs(row, coordinate)
    coordinate = column + 1
    if coordinate < n and not visits[row][coordinate] and l <= abs(a[row][column] - a[row][coordinate]) <= r:
        dfs(row, coordinate)


n, l, r = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]

times = 0
while True:
    movement, visits = False, [[False] * n for _ in range(n)]
    for row in range(n):
        for column in range(n):
            union = []
            dfs(row, column)
            if len(union) >= 2:
                population = 0
                for row, column in union:
                    population += a[row][column]
                population //= len(union)
                for row, column in union:
                    if population != a[row][column]:
                        a[row][column] = population
                        movement = True
    if movement:
        times += 1
    else:
        break

print(times)

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
