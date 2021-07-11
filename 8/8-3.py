# 호출되는 함수 확인
import time

start_time = time.time()

d = [0] * 100


def fibo(x):
    print(f"f({x})", end=' ')
    if x <= 2:
        return 1
    if d[x] <= 0:
        d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


fibo(6)

print(f"\ntime: {time.time() - start_time}")
