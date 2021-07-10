"""
부품 찾기 (집합 자료형 이용)

5
8 3 7 9 2
3
5 7 9
"""
import time

start_time = time.time()
n = int("5")
array = set(map(int, "8 3 7 9 2".split()))
m = int("3")
x = list(map(int, "5 7 9".split()))
for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
print(f"\ntime: {time.time() - start_time}")
