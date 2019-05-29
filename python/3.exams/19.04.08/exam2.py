import sys
import queue

def braces(values):
    result = []

    for string in values:
        dict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for i in range(0, len(string)):
            flag = False

            if string[i] is '{' or string[i] is '[' or string[i] is '(':
                stack.append(string[i])
            else:
                if not stack:
                    result.append('NO')
                    flag = True
                    break
                if stack.pop() is dict[string[i]]: # 같은 쌍임을 알려주는 것이 필요
                    continue
                else:
                    result.append('NO')
                    flag = True
                    break
        if stack and not flag:
            result.append('NO')
        elif not stack and not flag:
            result.append('YES')

    return result


if __name__ == '__main__':

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = braces(values)
    print(res)