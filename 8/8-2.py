# 피보나치 함수 소스코드
import time

start_time = time.time()

d = [0] * 100


def fibo(x):
    if x <= 2:
        return 1
    if d[x] <= 0:
        d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))

print(f"time: {time.time() - start_time}")
