def solution(survey, choices):
    answer = []

    indicators = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    scores = {1: (0, 3), 2: (0, 2), 3: (0, 1), 4: (0, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3)}

    for i in range(len(survey)):
        indicators[survey[i][scores[choices[i]][0]]] += scores[choices[i]][1]

    if indicators['R'] >= indicators['T']:
        answer.append('R')
    else:
        answer.append('T')
    if indicators['C'] >= indicators['F']:
        answer.append('C')
    else:
        answer.append('F')
    if indicators['J'] >= indicators['M']:
        answer.append('J')
    else:
        answer.append('M')
    if indicators['A'] >= indicators['N']:
        answer.append('A')
    else:
        answer.append('N')

    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
