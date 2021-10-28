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
    # 'x' + 원래 문자열은 몇의 시간복잡도 ??
    # while left:
    #     ans = left.pop() + ans
    #
    # while right:
    #     ans += right.pop()
    left.extend(reversed(right))
    print(''.join(left))


t = int(sys.stdin.readline().strip())
for _ in range(t):
    cmds = list(sys.stdin.readline().strip())
    solve()