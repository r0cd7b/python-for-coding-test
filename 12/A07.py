# 럭키 스트레이트
# 123402
# 7755
from sys import stdin

n = stdin.readline().rstrip()
middle = len(n) // 2

summary = 0
for i in range(middle):
    summary += int(n[i])
for i in range(middle, len(n)):
    summary -= int(n[i])

if summary:
    print("READY")
else:
    print("LUCKY")
