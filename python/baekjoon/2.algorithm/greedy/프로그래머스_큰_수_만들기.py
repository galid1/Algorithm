import sys


def solution(number, k):
    require = len(number) - k
    stack = []
    for i in range(len(number)):
        while stack:
            tail = stack.pop()

            if tail >= number[i]:
                stack.append(tail)
                break

            if len(stack) + len(number) - i < require:
                stack.append(tail)
                break

        stack.append(number[i])

    ans = ''
    for s in stack:
        ans += s


    print(ans[:require])


n, k = map(int, sys.stdin.readline().strip().split(" "))
num = sys.stdin.readline().strip()
solution(num, k)

