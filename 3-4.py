# 1이 될 때까지
import sys

n, k = map(int, sys.stdin.readline().split())

result = 0
while n >= k:
    target = n // k
    result += n - target * k
    n = target
    result += 1
result += n - 1

print(result)
'''
25 5

2
'''
