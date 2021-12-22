# 블록 이동하기
from collections import deque


def get_next_pos(pos, board):
    pos, dx, dy = list(pos), [-1, 1, 0, 0], [0, 0, -1, 1]
    pos1_x, pos1_y, pos2_x, pos2_y, next_pos = pos[0][0], pos[0][1], pos[1][0], pos[1][1], []
    for i in range(len(dx)):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = \
            pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if not (board[pos1_next_x][pos1_next_y] or board[pos2_next_x][pos2_next_y]):
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if not (board[pos1_x + i][pos1_y] or board[pos2_x + i][pos2_y]):
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    else:
        for i in [-1, 1]:
            if not (board[pos1_x][pos1_y + i] or board[pos2_x][pos2_y + i]):
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos


def solution(board):
    pos, length = {(1, 1), (1, 2)}, len(board) + 2
    q, new_board = deque([(pos, 0)]), [[1] * length] + [[1] + line + [1] for line in board] + [[1] * length]
    visited = [pos]
    while q:
        pos, cost = q.popleft()
        if (len(board), len(board)) in pos:
            return cost
        cost += 1
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost))
                visited.append(next_pos)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

"""
board
[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
Result
7
"""
