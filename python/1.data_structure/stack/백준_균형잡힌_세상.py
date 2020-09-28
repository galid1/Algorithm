# 백준 4949 균형잡힌 세상
import sys

sentence = 1
while sentence:
    sentence = sys.stdin.readline().rstrip().split(".")

    if not sentence[0]:
        break

    target = sentence[0]
    stack = []
    for c in target:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack:
                cur_b = stack.pop()
                if cur_b != '(':
                    stack.append(cur_b)
                    break
            else:
                stack.append(")")

        elif c == ']':
            if stack:
                cur_b = stack.pop()
                if cur_b != '[':
                    stack.append(cur_b)
                    break
            else:
                stack.append("]")

    if not stack:
        print('yes')
    else:
        print('no')

