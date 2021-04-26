import sys


def solve():
    global n, exp, nums

    # exp 숫자로 변경
    for i in range(len(exp)):
        if exp[i].isalpha():
            c = ord(exp[i]) - 65
            exp[i] = nums[c]

    # 계산
    a = ''
    stack = []
    for c in exp:
        if str(c).isdigit():
            stack.append(c)
        else:
            num2, num1 = float(stack.pop()), float(stack.pop())
            res = 0

            if c == '*':
                res = num1 * num2
            elif c == '/':
                res = num1 / num2
            elif c == '-':
                res = num1 - num2
            elif c == '+':
                res = num1 + num2

            stack.append(res)

    print(format(stack.pop(), '.2f'))


n = int(sys.stdin.readline().strip())
exp = list(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

solve()

