# 숨바꼭질
from sys import stdin
from heapq import heappush, heappop

n, m = map(int, stdin.readline().split())
barns: list = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    barns[a].append((1, b))
    barns[b].append((1, a))
heap, distances = [barn for barn in barns[0]], [0] + [19999] * (n - 1)
for distance, barn in barns[0]:
    distances[barn] = distance
while heap:
    distance_current, current_barn = heappop(heap)
    for distance_next, next_barn in barns[current_barn]:
        total_distance = distance_current + distance_next
        if distances[next_barn] > total_distance:
            heappush(heap, (total_distance, next_barn))
            distances[next_barn] = total_distance
distance, number, barn = distances[1], 1, 1
for i in range(2, n):
    if distances[i] > distance:
        distance, number, barn = distances[i], 1, i
    elif distances[i] == distance:
        number += 1
print(barn + 1, distance, number)

"""
입력 예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
출력 예시
4 2 3
"""
