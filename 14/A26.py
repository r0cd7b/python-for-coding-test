# 카드 정렬하기
from sys import stdin
import heapq

n, bundles = int(stdin.readline()), []
for _ in range(n):
    heapq.heappush(bundles, int(stdin.readline()))

number = 0
while len(bundles) >= 2:
    bundle = heapq.heappop(bundles) + heapq.heappop(bundles)
    heapq.heappush(bundles, bundle)
    number += bundle

print(number)

"""
입력 예시
3
10
20
40
출력 예시
100

입력 예시
4
10
20
40
50
출력 예시
220
"""
