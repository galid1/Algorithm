def isValid(s):
    stack = []

    for c in s:
        if is_open(c):
            stack.append(c)
            continue

        if not stack:
            return False

        if not is_pair(stack.pop(), c):
            return False

    if stack:
        return False

    return True


def is_open(bracket):
    return bracket == '(' or bracket == '{' or bracket == '['


def is_pair(bef_bracket, close_bracket):
    if close_bracket == ')':
        return bef_bracket == '('

    elif close_bracket == '}':
        return bef_bracket == '{'

    elif close_bracket == ']':
        return bef_bracket == '['

    return True



s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = '['

print(isValid(s))