# 감시 피하기
from sys import stdin
from itertools import combinations


def process():
    for teacher in teachers:

        x = teacher[0] - 1
        while x >= 0:
            if board[x][teacher[1]] == 'O':
                break
            if board[x][teacher[1]] == 'S':
                return False
            x -= 1

        x = teacher[0] + 1
        while x < n:
            if board[x][teacher[1]] == 'O':
                break
            if board[x][teacher[1]] == 'S':
                return False
            x += 1

        y = teacher[1] - 1
        while y >= 0:
            if board[teacher[0]][y] == 'O':
                break
            if board[teacher[0]][y] == 'S':
                return False
            y -= 1

        y = teacher[1] + 1
        while y < n:
            if board[teacher[0]][y] == 'O':
                break
            if board[teacher[0]][y] == 'S':
                return False
            y += 1

    return True


n, board, spaces, teachers = int(stdin.readline()), [], [], []
for i in range(n):
    board.append(stdin.readline().split())
    for j in range(n):
        if board[i][j] == 'X':
            spaces.append((i, j))
        elif board[i][j] == 'T':
            teachers.append((i, j))

for data in combinations(spaces, 3):
    for space in data:
        board[space[0]][space[1]] = 'O'

    if process():
        print("YES")
        break

    for space in data:
        board[space[0]][space[1]] = 'X'
else:
    print("NO")

'''
입력 예시 1
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
출력 예시 2
YES

입력 예시 2
4
S S S T
X X X X
X X X X
T T T X
출력 예시 2
NO
'''
