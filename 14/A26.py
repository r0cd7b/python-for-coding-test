# 카드 정렬하기
from sys import stdin
import heapq

n, bundles = int(stdin.readline()), []
for _ in range(n):
    heapq.heappush(bundles, int(stdin.readline()))

if n == 1:
    number = heapq.heappop(bundles)
else:
    number = 0
    for _ in range(n - 1):
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
3
3
3
3
출력 예시
24

입력 예시
4
30
40
50
100
출력 예시
410

입력 예시
4
30
40
50
60
출력 예시
360

입력 예시
20
224
653
518
407
195
811
821
589
678
738
530
301
714
304
588
669
219
318
442
866
출력 예시
44722
"""
