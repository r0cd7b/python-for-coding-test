# 괄호 변환
def solution(p):
    if not p:
        return p

    p_d, u, v = {'(': 0, ')': 0}, None, None
    for i in range(len(p)):
        p_d[p[i]] += 1
        if p_d['('] == p_d[')']:
            c_p = i + 1
            u, v = p[:c_p], p[c_p:]
            break

    p_d['('], p_d[')'] = 0, 0
    for pa in u:
        p_d[pa] += 1
        if p_d['('] < p_d[')']:
            p_d['('], p_d[')'], n_u = ')', '(', []
            for i in range(1, len(u) - 1):
                n_u.append(p_d[u[i]])
            return '(' + solution(v) + ')' + ''.join(n_u)
    return u + solution(v)


print(f'입력 예시 1\n"(()())()"\n출력 예시 1\n"(()())()" = "{solution("(()())()")}"')
print(f'입력 예시 2\n")("\n출력 예시 2\n"()" = "{solution(")(")}"')
print(f'입력 예시 3\n"()))((()"\n출력 예시 3\n"()(())()" = "{solution("()))((()")}"')
