# 에라토스테네스의 체
from math import sqrt

n = 1000
array = [True] * (n - 1)
for i in range(2, int(sqrt(n)) + 1):
    if array[i]:
        j = 2
        k = i * j
        while k <= n:
            array[k - 2] = False
            j += 1
            k = i * j
for i in range(len(array)):
    if array[i]:
        print(i + 2)
