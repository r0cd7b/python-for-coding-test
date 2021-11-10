# 연구소
from sys import stdin
from collections import deque
from copy import deepcopy

n, m = map(int, stdin.readline().split())

blanks, viruses, laboratory = [], [], []
for i in range(n):
    characters, line = stdin.readline().split(), []
    for j in range(m):
        line.append(int(characters[j]))
        if line[j] == 0:
            blanks.append((i, j))
        elif line[j] == 2:
            viruses.append((i, j))
    laboratory.append(line)

maximum = 0
for i in range(len(blanks) - 2):
    for j in range(i + 1, len(blanks) - 1):
        for k in range(j + 1, len(blanks)):
            inspection = deepcopy(laboratory)

            inspection[blanks[i][0]][blanks[i][1]], \
            inspection[blanks[j][0]][blanks[j][1]], \
            inspection[blanks[k][0]][blanks[k][1]] = 1, 1, 1

            queue = deque(viruses)
            while queue:
                current = queue.popleft()
                right, bottom, left, top = current[1] + 1, current[0] + 1, current[1] - 1, current[0] - 1
                if right < m and inspection[current[0]][right] == 0:
                    inspection[current[0]][right] = 2
                    queue.append((current[0], right))
                if bottom < n and inspection[bottom][current[1]] == 0:
                    inspection[bottom][current[1]] = 2
                    queue.append((bottom, current[1]))
                if left >= 0 and inspection[current[0]][left] == 0:
                    inspection[current[0]][left] = 2
                    queue.append((current[0], left))
                if top >= 0 and inspection[top][current[1]] == 0:
                    inspection[top][current[1]] = 2
                    queue.append((top, current[1]))

            safe = 0
            for x in range(n):
                for y in range(m):
                    if inspection[x][y] == 0:
                        safe += 1

            maximum = max(maximum, safe)

print(maximum)

'''
입력 예시 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
출력 예시 1
27

입력 예시 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
출력 예시 2
9

입력 예시 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
출력 예시 3
3
'''
