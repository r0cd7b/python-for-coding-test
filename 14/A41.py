# 여행 계획
from sys import stdin

n = int(stdin.readline().split()[0])
destinations, connections, plan = [list(map(int, stdin.readline().split())) for _ in range(n)], [i for i in range(n)], [
    int(s) - 1 for s in stdin.readline().split()]
for i in range(n - 1):
    for j in range(i + 1, n):
        if destinations[i][j]:
            connections[j] = connections[i]
for i in range(1, len(plan)):
    if connections[plan[0]] != connections[plan[i]]:
        print("NO")
        break
else:
    print("YES")

"""
입력 예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
출력 예시
YES
"""
