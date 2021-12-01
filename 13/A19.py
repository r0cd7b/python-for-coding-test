# 감시 피하기
from sys import stdin
from itertools import combinations


def check():
    for teacher in teachers:
        x = teacher[0] - 1
        while x >= 0:
            if hallway[x][teacher[1]] == 'O':
                break
            if hallway[x][teacher[1]] == 'S':
                return False
            x -= 1

        x = teacher[0] + 1
        while x < n:
            if hallway[x][teacher[1]] == 'O':
                break
            if hallway[x][teacher[1]] == 'S':
                return False
            x += 1

        y = teacher[1] - 1
        while y >= 0:
            if hallway[teacher[0]][y] == 'O':
                break
            if hallway[teacher[0]][y] == 'S':
                return False
            y -= 1

        y = teacher[1] + 1
        while y < n:
            if hallway[teacher[0]][y] == 'O':
                break
            if hallway[teacher[0]][y] == 'S':
                return False
            y += 1

    return True


n = int(stdin.readline())
hallway, teachers, blacks, students = [], [], [], 0
for x in range(n):
    hallway.append(stdin.readline().split())
    for y in range(n):
        if hallway[x][y] == 'T':
            teachers.append((x, y))
        elif hallway[x][y] == 'X':
            blacks.append((x, y))
        else:
            students += 1

for combination in combinations(blacks, 3):
    for blank in combination:
        hallway[blank[0]][blank[1]] = 'O'

    if check():
        print("YES")
        for information in hallway:
            print(information)
        break

    for blank in combination:
        hallway[blank[0]][blank[1]] = 'X'
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
