def solution(p):
    if not p:
        return p

    count, u, v = {'(': 0, ')': 0}, None, None
    for i in range(len(p)):
        count[p[i]] += 1
        if count['('] == count[')']:
            point = i + 1
            u, v = p[:point], p[point:]
            break

    count = 0
    for bracket in u:
        if bracket == '(':
            count += 1
        elif count == 0:
            new = []
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    new.append(')')
                else:
                    new.append('(')
            return '(' + solution(v) + ')' + ''.join(new)
        else:
            count -= 1
    return u + solution(v)


print(f'입력 예시 1\n"(()())()"\n출력 예시 1\n"(()())()" = "{solution("(()())()")}"')
print(f'입력 예시 2\n")("\n출력 예시 2\n"()" = "{solution(")(")}"')
print(f'입력 예시 3\n"()))((()"\n출력 예시 3\n"()(())()" = "{solution("()))((()")}"')
