from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
tube = [list(map(int, stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, stdin.readline().split())

viruses = []
for position_x in range(n):
    for position_y in range(n):
        if tube[position_x][position_y] > 0:
            viruses.append((tube[position_x][position_y], position_x, position_y))
viruses.sort()

viruses, old, second = deque(viruses), k, 0
while viruses:
    virus = viruses.popleft()

    if old == k and virus[0] == 1:
        if second >= s:
            break
        second += 1
    old = virus[0]

    up, down, left, right = virus[1] - 1, virus[1] + 1, virus[2] - 1, virus[2] + 1
    if up >= 0 and tube[up][virus[2]] <= 0:
        tube[up][virus[2]] = virus[0]
        viruses.append((tube[up][virus[2]], up, virus[2]))
    if down < n and tube[down][virus[2]] <= 0:
        tube[down][virus[2]] = virus[0]
        viruses.append((tube[down][virus[2]], down, virus[2]))
    if left >= 0 and tube[virus[1]][left] <= 0:
        tube[virus[1]][left] = virus[0]
        viruses.append((tube[virus[1]][left], virus[1], left))
    if right < n and tube[virus[1]][right] <= 0:
        tube[virus[1]][right] = virus[0]
        viruses.append((tube[virus[1]][right], virus[1], right))

print(tube[x - 1][y - 1])

'''
입력 예시 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2
출력 예시 1
3

입력 예시 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2
출력 예시 2
0
'''
