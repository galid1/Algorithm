def solution(w):
    # 빈 문자열
    if not w:
        return w

    # 이미 완성된 문자열
    if is_complete(w) and is_balanced(w):
        return w

    res = cut(w)

    return res


def cut(w):
    if not w:
        return w

    # 균형잡힌 u,v 로 분리 (w의 길이가 2인경우 할당이 안되므로 u를 w로 초기화)
    u = w
    v = ''

    for i in range(2, len(w), 2):
        temp_u = w[0:i]
        temp_v = w[i:]

        if is_balanced(temp_u):
            u = temp_u
            v = temp_v
            break

    if is_complete(u):
        return u + cut(v)
    else:
        return "(" + cut(v) + ")" + do_complete(u)


def is_balanced(u):
    ob = 0
    cb = 0
    for c in u:
        if c == '(':
            ob += 1
        else:
            cb += 1
    return ob == cb


def is_complete(u):
    if not u:
        return True

    stack = [u[0]]

    if len(u) == 1:
        return False

    for i in range(1, len(u)):
        c = u[i]
        if c == '(':
            stack.append(c)
        else: # )
            if not stack:
                return False
            elif stack.pop() == c:
                return False

    if stack:
        return False

    return True


# u의 첫번째, 마지막을 제거한후 괄호를 뒤집어서 반환
def do_complete(u):
    res = ""
    for c in u[1:-1]:
        if c == ')':
            res += '('
        else:
            res += ')'
    return res


# solution(')(')
# solution('()))((()')
# print(solution('()'))
# solution('')
solution("()(())))((")
