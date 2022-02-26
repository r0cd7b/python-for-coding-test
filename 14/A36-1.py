# 편집 거리
from sys import stdin

str1, str2 = stdin.readline(), stdin.readline()

n, m = len(str1), len(str2)
dp = [[i for i in range(m)]] + [[i] for i in range(1, n)]
for i in range(1, n):
    i_1 = i - 1
    for j in range(1, m):
        j_1 = j - 1
        if str1[i_1] == str2[j_1]:
            dp[i].append(dp[i_1][j_1])
        else:
            dp[i].append(min(dp[i][j_1], dp[i_1][j], dp[i_1][j_1]) + 1)

print(dp[-1][-1])

"""
cat
cut
1

sunday
saturday
3
"""
