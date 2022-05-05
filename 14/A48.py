# 어른 상어
from sys import stdin


def move():
    coordinates[number] = (x, y)
    directions[number] = direction


N, M, K = map(int, stdin.readline().split())
coordinates: dict[int, tuple[int, int]] = {}
spaces = [[-1] * N for _ in range(N)]
times = {}
for i in range(N):
    inputs = stdin.readline().split()
    for j in range(N):
        if inputs[j] != '0':
            number = int(inputs[j]) - 1
            coordinates[number] = (i, j)
            spaces[i][j] = number
            times[(i, j)] = K
directions = [int(input_) - 1 for input_ in stdin.readline().split()]
priorities = [[[int(input_) - 1 for input_ in stdin.readline().split()] for _ in range(4)] for _ in range(M)]

changes_direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(1, 1001):
    all_movements = []

    for number in coordinates:
        movements = []
        for direction in priorities[number][directions[number]]:
            x = coordinates[number][0] + changes_direction[direction][0]
            y = coordinates[number][1] + changes_direction[direction][1]
            if 0 <= x <= N - 1 >= y >= 0:
                movements.append((direction, x, y))
        for direction, x, y in movements:
            if spaces[x][y] < 0:
                all_movements.append((number, direction, x, y))
                break
        else:
            for direction, x, y in movements:
                if spaces[x][y] == number:
                    all_movements.append((number, direction, x, y))
                    break

    disappear = []
    for x, y in times:
        if times[(x, y)] < 2:
            spaces[x][y] = -1
            disappear.append((x, y))
        else:
            times[(x, y)] -= 1
    for x, y in disappear:
        del times[(x, y)]

    for number, direction, x, y in all_movements:
        if spaces[x][y] < 0:
            move()
            spaces[x][y] = number
            times[(x, y)] = K
        elif spaces[x][y] < number:
            del coordinates[number]
        elif spaces[x][y] == number:
            move()
            times[(x, y)] = K
        else:
            move()
            del coordinates[spaces[x][y]]
            spaces[x][y] = number

    if len(coordinates) < 2:
        print(i)
        break
else:
    print(-1)

"""
입력 예시 1
4 2 6
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
4 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
출력 예시 1
26

입력 예시 2
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
출력 예시 2
14
"""
