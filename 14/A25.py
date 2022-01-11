# 실패율
def solution(N, stages):
    stages.sort()
    index, rate = 0, []
    for i in range(1, N + 1):
        previous = index
        while len(stages) > index and i >= stages[index]:
            index += 1
        rate.append((-((index - previous) / (len(stages) - previous)), i))
    rate.sort()
    return [i[1] for i in rate]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4, 1, 2, 3]
