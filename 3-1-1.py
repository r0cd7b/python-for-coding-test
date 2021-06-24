# 거스름돈
import time

n = int(input())

start_time = time.time()

total_coins = 0
for coin in [500, 100, 50, 10]:
    total_coins += n // coin
    n %= coin
print(total_coins)

print(f"time: {time.time() - start_time}")
