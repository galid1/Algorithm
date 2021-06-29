def solution(s):
    stack = list(s)
    new_stack = []

    for i in range(len(s)):
        new_stack.append(stack.pop())

        if len(new_stack) >= 2 and new_stack[-1] == new_stack[-2]:
            new_stack.pop()
            new_stack.pop()

    if len(new_stack) == 0:
        return 1
    else:
        return 0


print(solution('cbaabaac'))