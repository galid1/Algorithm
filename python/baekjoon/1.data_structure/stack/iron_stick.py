# baekjoon 10799 쇠막대기

# 파이썬 리스트에는 다양한 형을 넣을수 있는걸 알지만 다른 언어에서를 고려해 문자열, 정수형 변환 코드를 넣음
import sys

def iron_stick(problem):
    before_bracket = problem.pop()
    stack = []
    result = 0

    while problem:
        new_bracket = problem.pop()

        # ( ) 레이저
        if before_bracket == '(' and new_bracket == ')':
            # 스택에 레이저만 들어있는 경우 continue
            if not stack:
                before_bracket = new_bracket
                continue

            # 첫 레이저
            if stack[-1] == 'ㅡ':
                stack.append('1')
            # 이미 레이저가 있던 경우
            else:
                laser_count = int(stack.pop()) + 1
                stack.append(str(laser_count))

        # ( ( 막대기
        elif before_bracket == '(' and new_bracket == '(':
            stack.append('ㅡ')
        # ) ( 기다려야됨
        elif before_bracket == ')' and new_bracket == '(':
            before_bracket = new_bracket
            continue
        # ) ) 막대기 하나가 끝남
        elif before_bracket == ')' and new_bracket == ')':
            laser_count = int(stack.pop())
            if stack:
                stack.pop() #막대기 제거
                result += laser_count + 1
                if stack:
                    if stack[-1] == 'ㅡ':
                        stack.append(str(laser_count))
                    else :
                        laser_count += int(stack.pop())
                        stack.append(str(laser_count))

        # 이전 괄호 바꾸기
        before_bracket = new_bracket

    print(result)


problem = list(sys.stdin.readline().rstrip())
problem.reverse()
iron_stick(problem)