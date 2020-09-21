def solution(s):
    answer = ''
    mid = len(s) // 2

    if len(s) < 2:
        return s

    # 짝수 글자
    if len(s)%2 == 0:
        answer = s[mid - 1] + s[mid]
    # 홀수 글자
    else:
        answer += s[mid]

    return answer


# print(solution('a'))
# print(solution('abcde'))
print(solution('qwer'))
