def solution(w):
    if not w:
        return w

    u, v = cut(w)

    if is_complete(u):
        v = solution(v)
        return u+v
    else:
        u = do_complete(u, v)

    print(u+v)
    return u+v


def cut(w):
    for i in range(2, len(w), 2):
        u = w[0:i]
        v = w[i:]

        if is_balanced(u):
            print('u: ', u)
            print("v : ", v)
            return u, v

    return '', ''


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
            if stack.pop() == c:
                return False

    if stack:
        return False

    return True


def do_complete(u, v):
    res = "(" + v + ")"

    for c in u[1:-1]:
        if c == ')':
            res += '('
        else:
            res += ')'
    return res



solution(')(')
# solution('()))((()')
# solution('()')