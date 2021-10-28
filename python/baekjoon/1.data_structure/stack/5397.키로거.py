import sys


def solve():
    global cmds

    left = []
    right = []

    for cmd in cmds:
        if cmd == '-':
            if left:
                left.pop()
            continue

        elif cmd == '<':
            if left:
                right.append(left.pop())

        elif cmd == '>':
            if right:
                left.append(right.pop())

        else:
            left.append(cmd)

    ans = ''

    ans = ''.join(left)
    right.reverse()
    ans += ''.join(right)
    print(ans)

    # left.extend(reversed(right))
    # print(''.join(left))


    # 'x' + 원래 문자열은 몇의 시간복잡도 ??, 아래 답변은 시간 초과가 발생함
    # while left:
    #     ans = left.pop() + ans
    #
    # while right:
    #     ans += right.pop()


t = int(sys.stdin.readline().strip())
for _ in range(t):
    cmds = list(sys.stdin.readline().strip())
    solve()