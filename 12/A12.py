# 기둥과 보 설치
def possible_pillar(wall, x, y, floor, pillar, beam):
    if y == floor or wall[x - 1][y] & beam or wall[x][y] & beam or wall[x][y - 1] & pillar:
        return True
    return False


def possible_beam(wall, x, y, pillar, beam):
    if wall[x][y - 1] & pillar or wall[x + 1][y - 1] & pillar or wall[x - 1][y] & beam and wall[x + 1][y] & beam:
        return True
    return False


def make_sure_rules(wall, start, end, floor, pillar, beam):
    for x in range(start, end):
        for y in range(start, end):
            if wall[x][y] & pillar and not possible_pillar(wall, x, y, floor, pillar, beam):
                return False
            if wall[x][y] & beam and not possible_beam(wall, x, y, pillar, beam):
                return False
    return True


def solution(n, build_frame):
    n += 3
    wall = [[0b00] * n for _ in range(n)]
    start, end = 1, n - 1
    floor = 1
    pillar, beam = 0b01, 0b10

    for x, y, a, b in build_frame:
        x, y = x + 1, y + 1
        if a:
            if b:
                if possible_beam(wall, x, y, pillar, beam):
                    wall[x][y] |= beam
            else:
                wall[x][y] ^= beam
                if not make_sure_rules(wall, start, end, floor, pillar, beam):
                    wall[x][y] |= beam
        else:
            if b:
                if possible_pillar(wall, x, y, floor, pillar, beam):
                    wall[x][y] |= pillar
            else:
                wall[x][y] ^= pillar
                if not make_sure_rules(wall, start, end, floor, pillar, beam):
                    wall[x][y] |= pillar

    answer = []
    for x in range(start, end):
        for y in range(start, end):
            real_x, real_y = x - 1, y - 1
            if wall[x][y] & pillar:
                answer.append([real_x, real_y, 0])
            if wall[x][y] & beam:
                answer.append([real_x, real_y, 1])
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print([[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
