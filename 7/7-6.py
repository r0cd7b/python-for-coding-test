"""
부품 찾기 (계수 정렬)

5
8 3 7 9 2
3
5 7 9
"""
import time

start_time = time.time()
n = int("5")
array = [0] * 1000000
for i in "8 3 7 9 2".split():
    array[int(i) - 1] = 1
m = int("3")
x = list(map(int, "5 7 9".split()))
for i in x:
    if array[i - 1]:
        print("yes", end=' ')
    else:
        print("no", end=' ')
print(f"\ntime: {time.time() - start_time}")
