def solution(input):
    inputs = input.split("\n")
    answer = inputs[0]
    m, n = map(int, inputs[0].split(" "))
    inputs = inputs[1:]

    exposed = [0 for _ in range(m)]
    day = 0
    visible = True
    for cmd in inputs:
        if not is_right_cmd(cmd):
            answer += "\nERROR"

        if cmd == 'EXIT':
            answer += "\nBYE"
            break

        if cmd == "SHOW":
            if not visible:
                answer += "\n0"
                continue
            answer += "\n1"
            exposed_cnt += 1
            if exposed_cnt >= n:
                visible = False

        if cmd == "NEXT":
            answer += "\n-"

            day += 1
            if day == m:
                day = -1
                exposed_cnt = 0
                visible = True

        if cmd == "NEGATIVE":
            answer += "\n0"
            visible = False


    return answer


def is_right_cmd(cmd):
    cmds = ['SHOW', 'NEXT', 'EXIT', 'NEGATIVE']
    return cmd in cmds


# e1 = "1 2\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW"
# print(solution(e1))

e2 = "2 3\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nEXIT"
print(solution(e2))

# e3 = "2 3\nSHOW\nNEGATIVE\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nEXIT"
# print(solution(e3))

# "2 3\n1\n1\n-\n1\n0\n-\n0\n-\n0\n0\n-\n1\nBYE"