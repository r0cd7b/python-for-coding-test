def produce(indicators, front, back, answer):
    if indicators[front] >= indicators[back]:
        answer.append(front)
    else:
        answer.append(back)


def solution(survey, choices):
    indicators, scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}, \
                         {1: (0, 3), 2: (0, 2), 3: (0, 1), 4: (0, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3)}
    for i in range(len(survey)):
        indicators[survey[i][scores[choices[i]][0]]] += scores[choices[i]][1]
    answer = []
    produce(indicators, 'R', 'T', answer)
    produce(indicators, 'C', 'F', answer)
    produce(indicators, 'J', 'M', answer)
    produce(indicators, 'A', 'N', answer)
    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
