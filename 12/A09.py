# 문자열 압축
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = 0
        prev = s[:step]
        count = 1
        for j in range(step, len(s) + step, step):
            if prev == s[j:j + step]:
                count += 1
                continue
            compressed += len(str(count)) + len(prev) if count >= 2 else len(prev)
            prev = s[j:j + step]
            count = 1
        answer = min(answer, compressed)
    return answer


print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)
