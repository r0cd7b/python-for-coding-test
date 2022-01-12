# 카드 정렬하기
from sys import stdin
import heapq

n, heap = int(stdin.readline()), []
for _ in range(n):
    heapq.heappush(heap, int(stdin.readline()))

result = 0
while len(heap) >= 2:
    sum_value = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, sum_value)
    result += sum_value

print(result)

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
