def solution(program, flag_rules, commands):
    answer = []

    flag_rules = make_dict_flag_rules(flag_rules)

    for command in commands:
        answer.append(verify_cmd(program, flag_rules, command))

    print(answer)
    return answer


def make_dict_flag_rules(flag_rules):
    dict_flag_rules = {}

    for rule in flag_rules:
        flag, arg_type = rule.split(" ")
        dict_flag_rules[flag] = arg_type

    return dict_flag_rules


def verify_cmd(program, flag_rules, command):
    cmd_name, flags = command.split(" ")[0], command.split(" ")[1:]

    if not verify_program_name(program, cmd_name):
        return False
    if not verify_flags(flag_rules, flags):
        return False

    return True


def verify_program_name(program, cmd_name):
    correct = False
    if program == cmd_name:
        correct = True

    return correct


def verify_flags(flag_rules, input_flags):
    used_flag = {}
    turn = "FLAG"
    cur_flag_type = None

    for i in range(len(input_flags)):
        element = input_flags[i]

        # flag_name
        if element.startswith('-'):
            # Value가 나와야 할 차례
            if turn == "VALUE":
                return False

            # 이미 사용된 flag
            if element in used_flag.keys():
                return False

            # 존재하지 않는 flag
            if element not in flag_rules.keys():
                return False
            else:
                cur_flag_type = flag_rules[element]
                used_flag[element] = True
                turn = "VALUE"

        # flag_type
        else:
            # FLAG가 나와야 할 차례
            if turn == "FLAG":
                return False

            if cur_flag_type == None:
                turn = "FLAG"
                continue
            # int 면 digit
            elif cur_flag_type == "STRING":
                if element.isdigit():
                    return False
            elif cur_flag_type == "STRINGS":
                if element.isdigit():
                    return False
                turn = "NO_MATTER"
                continue

            elif cur_flag_type == "NUMBER":
                if not element.isdigit():
                    return False
            elif cur_flag_type == "NUMBERS":
                if not element.isdigit():
                    return False
                turn = "NO_MATTER"
                continue

            turn = "FLAG"

    return True


program = "line"
flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]
solution(program, flag_rules, commands)

program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
solution(program, flag_rules, commands)