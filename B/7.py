# 순열과 조합
from itertools import permutations

for x in permutations([1, 2], 2):
    x: list[int] = list(x)
    print(x)
