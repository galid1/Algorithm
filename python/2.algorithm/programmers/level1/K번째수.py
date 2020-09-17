# 프로그래머스 i번째 j번째까지 자르고 정렬한뒤 k번째 수 구하기

def solution(array, commands):
    answer = []

    for command in commands:
        sub_solution(answer, array, command)

    return answer


def sub_solution(answer, array, command):
    first = command[0] - 1
    last = command[1]
    sub_str = sorted(array[first:last])

    k = command[2]
    answer.append(sub_str[k-1])


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

