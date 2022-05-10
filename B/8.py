# 순열과 조합
from itertools import combinations

for x in combinations([1, 2, 3], 2):
    print(list(x), end=' ')
