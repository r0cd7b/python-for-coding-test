# 숫자 카드 게임
import time

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

start_time = time.time()

for i in data:
    i.sort()
data.sort(key=lambda j: j[0], reverse=True)
print(data[0][0])

print(f"time: {time.time() - start_time}")
