# 피보나치 함수 소스코드
import time

start_time = time.time()


def fibo(x):
    if x <= 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

print(f"time: {time.time() - start_time}")
