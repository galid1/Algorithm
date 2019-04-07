import math
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    dict = {")" : "(", "]" : "[", "}" : "{"}

    for i in range(0, len(s)):
        if s[i] is '{' or s[i] is '[' or s[i] is '(':
            stack.append(s[i])
        else:
            if not stack:
                return 'NO'
            if stack.pop() is dict[s[i]]: # 같은 쌍임을 알려주는 것이 필요
                continue
            else:
                return 'NO'
    if stack:
        return 'NO'

    return 'YES'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)