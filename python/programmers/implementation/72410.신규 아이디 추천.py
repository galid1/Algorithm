def solution(new_id):
    cant = list('~!@#$%^&*()=+[{]}:?,<>/')

    answer = ''

    for idx, c in enumerate(list(new_id)):
        if not answer and c == '.':
            continue

        if c in cant:
            continue

        if len(answer) >= 1 and answer[-1] == '.' and c == '.':
            continue

        if str(c).isupper():
            c = c.lower()
        answer += c

    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = 'a'
    else:
        if len(answer) > 15:
            answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]

    answer += answer[-1] * (3 - len(answer))

    return answer


# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = '.....'
new_id = 'asdb.'
new_id = 'ASDzccbva..a.a&!'
new_id = "123_.def"
new_id ="abcdefghijklmn.p"

new_id = ''
new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = "=.="

print(solution(new_id))
