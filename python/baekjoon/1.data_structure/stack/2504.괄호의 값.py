import sys


def solve():
    global bs

    stack = []
    for b in bs:
        if is_open(b):
            stack.append(b)

        else:
            cur = 0
            closed = False
            while stack:
                target = stack.pop()

                if type(target) == int:
                    cur += target
                    continue

                if verify_pair(b, target):
                    closed = True

                    if cur == 0:
                        stack.append(get_score(b))
                    else:
                        stack.append(get_score(b) * cur)
                break

            if not closed:
                return 0

    ans = 0
    while stack:
        item = stack.pop()
        if type(item) != int:
            return 0

        ans += item

    return ans


def is_open(bracket):
    return bracket == '(' or bracket == '['


def verify_pair(bracket, target):
    if bracket == ')':
        return target == '('

    if bracket == ']':
        return target == '['


def get_score(bracket):
    if bracket == ')':
        return 2

    if bracket == ']':
        return 3



bs = list(sys.stdin.readline().strip())
print(solve())
