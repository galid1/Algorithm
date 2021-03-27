import sys

def solve(idx, cur_num):
    global operators, operands, ans

    if idx >= len(operators):
        ans = max(ans, cur_num)
        return

    solve(idx+1, cal(operators[idx], cur_num, operands[idx+1]))

    if idx+1 < len(operators):
        bracket_res = cal(operators[idx+1], operands[idx+1], operands[idx+2])
        solve(idx+2, cal(operators[idx], cur_num, bracket_res))


def cal(op, operand1, operand2):
    if op == '+':
        return operand1 + operand2
    elif op == '*':
        return operand1 * operand2
    elif op == '-':
        return operand1 - operand2


n = int(sys.stdin.readline().strip())
strs = list(sys.stdin.readline().strip())
ans = -sys.maxsize - 1
operators = []
operands = []
for i in range(len(strs)):
    if i % 2 == 0:
        operands.append(int(strs[i]))
    else:
        operators.append(strs[i])

solve(0, operands[0])
print(ans)