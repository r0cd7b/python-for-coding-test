# 실패율
def solution(N, stages):
    length, answer = len(stages), []
    for i in range(1, N + 1):
        count = stages.count(i)
        if length:
            answer.append((-(count / length), i))
        else:
            answer.append((0, i))
        length -= count
    return [i[1] for i in sorted(answer)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4, 1, 2, 3]
