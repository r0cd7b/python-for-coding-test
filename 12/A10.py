# 자물쇠와 열쇠
def check(lock, start, end):
    for i in range(start, end):
        for j in range(start, end):
            if lock[i][j] != 1:
                return False
    return True


def move_check(lock, start, end, key):
    for x in range(end):
        for y in range(end):

            for i in range(len(key)):
                for j in range(len(key)):
                    lock[x + i][y + j] += key[i][j]

            if check(lock, start, end):
                return True

            for i in range(len(key)):
                for j in range(len(key)):
                    lock[x + i][y + j] -= key[i][j]

    return False


def solution(key, lock):
    if check(lock, 0, len(lock)):
        return True

    lock_start = len(key) - 1
    lock_end = lock_start + len(lock)
    new_lock_size = lock_end + lock_start
    new_lock = [[0] * new_lock_size for _ in range(new_lock_size)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[lock_start + i][lock_start + j] = lock[i][j]

    if move_check(new_lock, lock_start, lock_end, key):
        return True

    for _ in range(3):
        rotated_key = [[0] * len(key) for _ in key]
        for i in range(len(key)):
            for j in range(len(key)):
                rotated_key[i][j] = key[len(key) - 1 - j][i]
        key = rotated_key

        if move_check(new_lock, lock_start, lock_end, key):
            return True
    return False


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) is False)
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) is False)
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) is True)

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) is False)
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) is True)
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) is True)

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) is True)
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) is False)
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) is True)
