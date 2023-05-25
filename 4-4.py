# 게임 개발
import sys

strings = sys.stdin.readline().split()
n = int(strings[0])
m = int(strings[1])
strings = sys.stdin.readline().split()
a = int(strings[0])
b = int(strings[1])
d = int(strings[2])

movements, map_ = ((-1, 0), (0, 1), (1, 0), (0, -1)), [sys.stdin.readline().split() for _ in range(n)]
map_[a][b], visited = '2', 1
while True:
    for _ in range(4):
        d = (d + 3) % 4
        vertically, horizontally = movements[d]
        next_a, next_b = a + vertically, b + horizontally
        if map_[next_a][next_b] == '0':
            a, b = next_a, next_b
            map_[a][b] = '2'
            visited += 1
            break
    else:
        vertically, horizontally = movements[d]
        next_a, next_b = a - vertically, b - horizontally
        if map_[next_a][next_b] != '1':
            a, b = next_a, next_b
        else:
            break

print(visited)
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

3

4 6
1 1 0
1 1 1 1 1 1
1 0 0 0 0 1
1 1 0 1 0 1
1 1 1 1 1 1
'''
