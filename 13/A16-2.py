# 연구소
n, m = map(int, input().split())
data, temp, dx, dy, result = [], [[0] * m for _ in range(n)], [-1, 0, 1, 0], [0, 1, 0, -1], 0

for _ in range(n):
    data.append(list(map(int, input().split())))


def virus(x, y):
    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count != 3:
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j], count = 1, count + 1
                    dfs(count)
                    data[i][j], count = 0, count - 1
        return
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)
    result = max(result, get_score())


dfs(0)
print(result)

'''
입력 예시 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
출력 예시 1
27

입력 예시 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
출력 예시 2
9

입력 예시 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
출력 예시 3
3
'''
