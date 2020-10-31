# 아스키 코드로
def to_ord(a):
    return (ord(a)-97)%26 + 1


# 알파벳으로
def to_chr(d):
    return chr((d - 1) % 26 + 97)


def r_rot(s, n):
    # for 말고, rotation 만큼 문자열을 잘라서 붙이는 방법도 있음 우선 이렇게
    if n > 0:
        for i in range(abs(n)):
            s = s[1:] + s[0]
    else: #-3 이었으니 다시 정방향으로
        for i in range(abs(n)):
            s = s[-1] + s[:-1]

    return s


def solution(encrypted_text, key, rotation):
    # 1. 역회전
    text = r_rot(encrypted_text, rotation)

    # 2. 역 움직임
    answer = ''
    for i in range(len(text)):
        answer += to_chr(to_ord(text[i]) - to_ord(key[i]))

    return answer


print(solution('ebcd', 'aaaa', -3))
# print(solution('dddd', 'cccc', -2))
# print(solution("c", 'a', -1))
# print(solution('aap', 'abc', -5))
# print(solution('hello', 'abcde', 5))
