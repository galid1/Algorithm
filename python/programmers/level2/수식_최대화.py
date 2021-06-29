def solution(exp):
    # 우선순위 경우의수 모두 구하기
    op = ['*', '+', '-']
    visit = [0 for i in range(len(op))]
    priorities = []
    make_priority(priorities, visit, op, priority=[])

    # 최초 연산자와 피연산자가 나뉜 스택
    num_stack = []
    op_stack = []
    make_first_stack(num_stack, op_stack, exp)

    # 우선순위에 따른 연산
    answers = []
    for i in range(len(priorities)):
        answers.append(calculate(priorities[i], num_stack.copy(), op_stack.copy()))

    # 결과 반환
    answers = list(map(abs, answers))
    answer = max(answers)
    return answer


def make_priority(priorities, visit, op, priority):
    if len(priority) == len(op):
        priorities.append(priority.copy())

    for i in range(len(op)):
        if not visit[i]:
            visit[i] = 1
            priority.append(op[i])
            make_priority(priorities, visit, op, priority)
            visit[i] = 0
            priority.pop()


def calculate(priority, num_stack, op_stack):
    # 연산자 수만큼 반복
    for j in range(len(priority)):
        cur_op = priority[j]

        t_n_stack = []
        t_op_stack = []
        for k in range(len(num_stack)):
            if not t_n_stack:
                t_n_stack.append(num_stack[k])
                continue

            if not op_stack:
                break

            op = op_stack[k-1]
            if op == cur_op:
                t_n_stack.append(cal(int(t_n_stack.pop()), int(num_stack[k]), op))
            else:
                t_n_stack.append(num_stack[k])
                t_op_stack.append(op_stack[k-1])

        num_stack = t_n_stack
        op_stack = t_op_stack

    ans = num_stack[0]
    return ans


def make_first_stack(num_stack, op_stack, exp):
    # 최초 수식을 스택으로 옮김
    idx = 0
    while idx < len(exp):
        if exp[idx].isdigit():
            num = ''
            while idx < len(exp) and exp[idx].isdigit():
                num += exp[idx]
                idx += 1
            num_stack.append(num)
        else:
            op_stack.append(exp[idx])
            idx += 1


def cal(num1, num2, op):
    if op == '*':
        return num1 * num2
    elif op == '-':
        return num1 - num2
    elif op == '+':
        return num1 + num2


solution('100-200*300-500+20')
solution('50*6-3*2')