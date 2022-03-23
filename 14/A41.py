# 여행 계획
from sys import stdin

n, m = map(int, stdin.readline().split())
parent = [i for i in range(n)]
for i in range(n):
    data = list(map(int, stdin.readline().split()))
    for j in range(i + 1, n):
        if data[j]:
            parent[j] = parent[i]
plan = [int(s) - 1 for s in stdin.readline().split()]
for i in range(1, m):
    if parent[plan[i]] != parent[plan[0]]:
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
