# 괄호 변환
def balanced_index(p):
    count = {'(': 0, ')': 0}
    for i in range(len(p)):
        count[p[i]] += 1
        if count['('] == count[')']:
            return i


def check_proper(p):
    count = {'(': 0, ')': 0}
    for i in range(len(p)):
        count[p[i]] += 1
        if count['('] < count[')']:
            return False
    return True


def solution(p):
    if not p:
        return p
    index = balanced_index(p) + 1
    u, v = p[:index], p[index:]
    if check_proper(u):
        return u + solution(v)
    p_d, n_u = {'(': ')', ')': '('}, []
    for i in range(1, len(u) - 1):
        n_u.append(p_d[u[i]])
    return '(' + solution(v) + ')' + ''.join(n_u)


print(f'입력 예시 1\n"(()())()"\n출력 예시 1\n"(()())()" = "{solution("(()())()")}"')
print(f'입력 예시 2\n")("\n출력 예시 2\n"()" = "{solution(")(")}"')
print(f'입력 예시 3\n"()))((()"\n출력 예시 3\n"()(())()" = "{solution("()))((()")}"')
