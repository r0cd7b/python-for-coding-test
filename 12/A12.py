# 기둥과 보 설치
def solution(n, build_frame):
    n += 5
    wall = [[0b00] * n for _ in range(n)]
    pillar, beam = 0b01, 0b10

    for x, y, a, b in build_frame:
        x, y = x + 2, y + 2
        if a:
            if b:
                if wall[x][y - 1] & pillar or \
                        wall[x + 1][y - 1] & pillar or \
                        wall[x - 1][y] & beam and wall[x + 1][y] & beam:
                    wall[x][y] |= beam
            else:
                if not (not wall[x - 1][y - 1] & pillar and
                        not wall[x][y - 1] & pillar and
                        not wall[x + 1][y - 1] & pillar
                        or
                        not wall[x][y - 1] & pillar and
                        not wall[x + 1][y - 1] & pillar and
                        not wall[x + 2][y - 1] & pillar):
                    wall[x][y] ^= beam
        else:
            if b:
                if y == 2 or \
                        wall[x][y] & beam or \
                        wall[x - 1][y] & beam or \
                        wall[x][y - 1] & pillar:
                    wall[x][y] |= pillar
            else:
                if not (wall[x][y + 1] & pillar
                        or
                        not wall[x - 1][y] & pillar and
                        wall[x - 1][y + 1] & beam and
                        not wall[x][y + 1] & beam
                        or
                        not wall[x - 1][y + 1] & beam and
                        wall[x][y + 1] & beam and
                        not wall[x + 1][y] & pillar):
                    wall[x][y] ^= pillar

    answer = []
    for x in range(2, n - 2):
        for y in range(2, n - 2):
            if wall[x][y] & pillar:
                answer.append([x - 2, y - 2, 0])
            if wall[x][y] & beam:
                answer.append([x - 2, y - 2, 1])
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print([[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
