def solution(program, flag_rules, commands):
    answer = []

    flag_rules = make_dict_flag_rules(flag_rules)

    for command in commands:
        answer.append(verify_cmd(program, flag_rules, command))

    return answer


def make_dict_flag_rules(flag_rules):
    dict_flag_rules = {}

    for rule in flag_rules:
        flag, arg_type = rule.split(" ")
        if arg_type == 'STRING':
            dict_flag_rules[flag] = str
        elif arg_type == 'NUMBER':
            dict_flag_rules[flag] = int
        else:
            dict_flag_rules[flag] = None

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
            elif cur_flag_type == str:
                if element.isdigit():
                    return False
            elif cur_flag_type == int:
                if not element.isdigit():
                    return False
            turn = "FLAG"

    return True





program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]
solution(program, flag_rules, commands)