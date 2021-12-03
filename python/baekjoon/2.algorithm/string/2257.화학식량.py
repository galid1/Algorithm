import sys


def solve():
    global s

    maps = {'C': '12', 'H': '1', 'O': '16'}

    ans = 0
    stack = []

    for c in s:
        if c.isalpha():
            stack.append(int(maps[c]))

        elif c == '(':
            stack.append(c)

        elif c == ')':
            tmp_sum = 0

            while stack:
                t_top = stack.pop()
                if t_top == '(':
                    break
                tmp_sum += int(t_top)

            if tmp_sum != 0:
                stack.append(tmp_sum)

        elif c.isnumeric():
            stack.append(int(c) * int(stack.pop()))

    while stack:
        ans += stack.pop()
    print(ans)

s = list(sys.stdin.readline().strip())
solve()