def solution(s):
    answer = True

    if not s.isdigit():
        return False

    if len(s) != 4 and len(s) != 6:
        return False

    return answer


solution("1234")
solution("123456")
solution('12345')