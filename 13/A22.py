# 블록 이동하기
from collections import deque


def solution(board):
    length = len(board) + 2
    board = [[1] * length] + \
            [[1, 0b010] + [board[0][i] for i in range(1, len(board[0]))] + [1]] + \
            [[1] + board[i] + [1] for i in range(1, len(board))] + \
            [[1] * length]
    queue, n, n_1 = deque([(1, 1, 0, 0)]), len(board) - 2, len(board) - 3
    while queue:
        x, y, orientation, time = queue.popleft()

        previous_x, next_x, previous_y, next_y, next_orientation, next_time = \
            x - 1, x + 1, y - 1, y + 1, -orientation + 1, time + 1
        if orientation:
            if x == n_1 and y == n:
                return time

            if not board[previous_x][y] & 0b101:
                board[previous_x][y] |= 0b100
                queue.append((previous_x, y, orientation, next_time))
            if not (board[next_x][y] & 0b100 or board[next_x + 1][y] & 0b001):
                board[next_x][y] |= 0b100
                queue.append((next_x, y, orientation, next_time))
            if not (board[x][previous_y] & 0b101 or board[next_x][previous_y] & 0b001):
                board[x][previous_y] |= 0b100
                queue.append((x, previous_y, orientation, next_time))
            if not (board[x][next_y] & 0b101 or board[next_x][next_y] & 0b001):
                board[x][next_y] |= 0b100
                queue.append((x, next_y, orientation, next_time))

            if not (board[x][previous_y] & 0b001 or board[next_x][previous_y] & 0b001):
                if not board[x][previous_y] & 0b010:
                    board[x][previous_y] |= 0b010
                    queue.append((x, previous_y, next_orientation, next_time))
                if not board[next_x][previous_y] & 0b010:
                    board[next_x][previous_y] |= 0b010
                    queue.append((next_x, previous_y, next_orientation, next_time))
            if not (board[x][next_y] & 0b001 or board[next_x][next_y] & 0b001):
                if not board[x][y] & 0b010:
                    board[x][y] |= 0b010
                    queue.append((x, y, next_orientation, next_time))
                if not board[next_x][y] & 0b010:
                    board[next_x][y] |= 0b010
                    queue.append((next_x, y, next_orientation, next_time))
        else:
            if x == n and y == n_1:
                return time

            if not (board[previous_x][y] & 0b011 or board[previous_x][next_y] & 0b001):
                board[previous_x][y] |= 0b010
                queue.append((previous_x, y, orientation, next_time))
            if not (board[next_x][y] & 0b011 or board[next_x][next_y] & 0b001):
                board[next_x][y] |= 0b010
                queue.append((next_x, y, orientation, next_time))
            if not board[x][previous_y] & 0b011:
                board[x][previous_y] |= 0b010
                queue.append((x, previous_y, orientation, next_time))
            if not (board[x][next_y] & 0b010 or board[x][next_y + 1] & 0b001):
                board[x][next_y] |= 0b010
                queue.append((x, next_y, orientation, next_time))

            if not (board[previous_x][y] & 0b001 or board[previous_x][next_y] & 0b001):
                if not board[previous_x][y] & 0b100:
                    board[previous_x][y] |= 0b100
                    queue.append((previous_x, y, next_orientation, next_time))
                if not board[previous_x][next_y] & 0b100:
                    board[previous_x][next_y] |= 0b100
                    queue.append((previous_x, next_y, next_orientation, next_time))
            if not (board[next_x][y] & 0b001 or board[next_x][next_y] & 0b001):
                if not board[x][y] & 0b100:
                    board[x][y] |= 0b100
                    queue.append((x, y, next_orientation, next_time))
                if not board[x][next_y] & 0b100:
                    board[x][next_y] |= 0b100
                    queue.append((x, next_y, next_orientation, next_time))


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

"""
board
[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
Result
7
"""
