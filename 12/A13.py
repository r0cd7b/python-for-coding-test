# 치킨 배달
from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
houses, chicken_houses = [], []
for r in range(n):
    buildings = list(map(int, stdin.readline().split()))
    for c in range(n):
        if buildings[c] == 1:
            houses.append((r, c))
        elif buildings[c] == 2:
            chicken_houses.append((r, c))

minimum_sum = 1e9
for number_draw in range(1, m + 1):
    for chicken_houses_combination in combinations(chicken_houses, number_draw):
        distance_sum = 0
        for r1, c1 in houses:
            minimum_distance = 1e9
            for r2, c2 in chicken_houses_combination:
                minimum_distance = min(minimum_distance, abs(r1 - r2) + abs(c1 - c2))
            distance_sum += minimum_distance
        minimum_sum = min(minimum_sum, distance_sum)

print(minimum_sum)

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
