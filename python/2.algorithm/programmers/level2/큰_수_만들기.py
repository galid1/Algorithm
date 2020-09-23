def solution(numbers, k):
    stack = [numbers[0]]

    for i in range(1, len(numbers)):
        stack.append(numbers[i])

        if k == 0:
            stack += numbers[i+1:]
            break

        stack_top = numbers[i]
        for j in range(len(stack)-2, -1, -1):
            if k == 0:
                break

            if stack_top > stack[j]:
                stack[j] = stack_top
                stack.pop()
                k -= 1
            else:
                break

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

print(solution('4177252841', 4))
print(solution('999', 2))
print(solution('999991', 3))
print(solution('111119', 3))