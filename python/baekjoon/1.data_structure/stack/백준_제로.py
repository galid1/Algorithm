# baekjoon 10773 제로
# 1. 수가 나오면 append
# 2. 0이 나오면 최근 수 뺀다
# 3. stack의 수들을 더한다

import sys

def solution(n):
    stack = []
    for i in range(n):
        num = int(sys.stdin.readline())

        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))


n = int(sys.stdin.readline())
solution(n)
