# 치킨 배달
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
chicken, houses = [], []
for r in range(n):
    data = list(map(int, stdin.readline().split()))
    for c in range(n):
        if data[c] == 1:
            houses.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

distances = 1e9
for number in range(1, m + 1):
    for candidates in combinations(chicken, number):
        result = 0
        for hx, hy in houses:
            temp = 1e9
            for cx, cy in candidates:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            result += temp
        distances = min(distances, result)

print(distances)

'''
입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
출력 예시 1
5

입력 예시 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
출력 예시 2
10

입력 예시 3
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
출력 예시 3
11

입력 예시 4
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
출력 예시 4
32
'''
