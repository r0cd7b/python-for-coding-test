def solution(places):
    answer = [0] * 5
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[j][k] == 'P':
                    x = j - 1
                    if x >= 0:
                        if places[x][k] == 'P':
                            break
                        # if places[x][k] == 'O':
                        #     if
            else:
                continue
            break
        else:
            answer[i] = 1
    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    )
)
