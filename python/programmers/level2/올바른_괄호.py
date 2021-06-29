def solution(s):
    answer = True
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False

            if stack[-1] == ')':
                return False
            else:
                stack.pop()

    if stack:
        return False

    return answer

solution('()()')
solution('(')
solution(")")