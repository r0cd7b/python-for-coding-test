# 자물쇠와 열쇠
def check(start, end, new_lock):
    for i in range(start, end):
        for j in range(start, end):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    if check(0, 0, lock):
        return True

    lock_start = len(key) - 1
    lock_end = lock_start + len(lock)

    new_lock_size = lock_end + lock_start
    new_lock = [[0] * new_lock_size for _ in range(new_lock_size)]
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            new_lock[i][j] = lock[i][j]

    for _ in range(3):

        for x in range(lock_end):
            for y in range(lock_end):

                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x + i][y + j] += key[i][j]

                if check(lock_start, lock_end, new_lock):
                    return True

                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x + i][y + j] -= key[i][j]

        rotated_key = [[0] * len(key) for _ in key]
        for i in range(len(key)):
            for j in range(len(key)):
                rotated_key[i][j] = key[len(key) - 1 - j][i]
        key = rotated_key

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) is True)
