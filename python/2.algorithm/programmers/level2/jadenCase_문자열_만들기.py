def solution(s):
    s = s.lower()
    s_list = s.split(" ")

    answer = ''

    for si in s_list:
        if not si:
            answer += ' '
            continue

        first_c = si[0]
        if first_c.isalpha():
            first_c = first_c.upper()

        answer += first_c + si[1:] + " "

    return answer[:-1]


# 처음과 끝이 공백인 경우는 존재하지 않음
# solution('3people unFollowed me')
# solution('for the last week')
# solution('a')
# solution('1')
# solution('A')
# solution('a1a1aa2')
# solution('A  b  c')
# solution('a  A1  Abc  cBc  asd  cBB')
# solution('a        b')
# solution('aa 1as 3ds')