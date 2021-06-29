import sys


def solve():
    global expression

    stack = []
    ans = ''
    for c in expression:
        if c.isalpha():
            ans += c
        else:
            # 여는
            if is_bracket(c) == 1:
                stack.append(c)
            # 닫는
            elif is_bracket(c) == -1:
                pop = stack.pop()
                while stack and not is_bracket(pop) == 1:
                    ans += pop
                    pop = stack.pop()

            # 연산자
            else:
                if not stack:
                    stack.append(c)
                    continue

                if c == '+' or c == '-':
                    while stack and stack[-1] != '(':
                        ans += stack[-1]
                        stack.pop()
                elif c == '*' or c == '/':
                    while stack and stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-':
                        ans += stack[-1]
                        stack.pop()

                stack.append(c)

    while stack:
        ans += stack.pop()
    print(ans)


def is_bracket(c):
    if c == '(':
        return 1
    elif c == ')':
        return -1
    else:
        return 0


expression = list(sys.stdin.readline().strip())
solve()
