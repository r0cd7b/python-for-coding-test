def solution(p: str):
    if not p:
        return p

    count, u, v = {'(': 0, ')': 0}, None, None
    for i in range(len(p)):
        count[p[i]] += 1
        if count['('] == count[')']:
            point = i + 1
            u, v = p[:point], p[point:]
            break

    stack = []
    for bracket in u:
        if bracket == '(':
            stack.append(bracket)
        elif stack:
            stack.pop()
        else:
            new = []
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    new.append(')')
                else:
                    new.append('(')
            return '(' + solution(v) + ')' + ''.join(new)
    return u + solution(v)


print(f'입력 예시 1\n"(()())()"\n출력 예시 1\n"(()())()" = "{solution("(()())()")}"')
print(f'입력 예시 2\n")("\n출력 예시 2\n"()" = "{solution(")(")}"')
print(f'입력 예시 3\n"()))((()"\n출력 예시 3\n"()(())()" = "{solution("()))((()")}"')
