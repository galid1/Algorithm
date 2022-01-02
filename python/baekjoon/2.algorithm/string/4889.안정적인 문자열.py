import sys


def solve(s):
    stack = []
    o_cnt, c_cnt = 0, 0

    for b in s:
        if not stack:
            stack.append(b)
            if b == "{":
                o_cnt += 1
            elif b == "}":
                c_cnt += 1
            continue

        if b == "{":
            stack.append(b)
            o_cnt += 1

        elif b == "}":
            if stack[-1] == "{":
                o_cnt -= 1
                stack.pop()
                continue

            else:
                stack.append(b)
                c_cnt += 1

    return o_cnt // 2 + o_cnt % 2 + c_cnt // 2 + c_cnt % 2


idx = 0
while True:
    idx += 1
    s = list(sys.stdin.readline().strip())

    if s[0] == '-':
        break

    ans = solve(s)
    print('{idx}. {ans}'.format(idx=idx, ans=ans))
