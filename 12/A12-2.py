# 기둥과 보 설치
def possible(answer):
    for x, y, stuff in answer:
        if stuff:
            if not ([x, y - 1, 0] in answer or
                    [x + 1, y - 1, 0] in answer or
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                return False
        else:
            if not (y == 0 or
                    [x - 1, y, 1] in answer or
                    [x, y, 1] in answer or
                    [x, y - 1, 0] in answer):
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        structure = [x, y, stuff]
        if operate:
            answer.append(structure)
            if not possible(answer):
                answer.remove(structure)
        else:
            answer.remove(structure)
            if not possible(answer):
                answer.append(structure)
    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
print([[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
