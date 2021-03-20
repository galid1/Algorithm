def solution(program, flag_rules, commands):
    answer = []

    flag_rules = make_dict_flag_rules(flag_rules)
    for command in commands:
        answer.append(verify_cmd(program, flag_rules, command))

    print(answer)
    return answer


def make_dict_flag_rules(flag_rules):
    dict_flag_rules = {}
    alias_rules = []

    for rule in flag_rules:
        split_rule = rule.split(" ")

        if len(split_rule) == 2:
            flag, arg_type = split_rule[0], split_rule[1]
            dict_flag_rules[flag] = arg_type
        # alias를 다루는 경우
        elif len(split_rule) == 3:
            alias_rules.append(split_rule)

    apply_alias_rules(dict_flag_rules, alias_rules)

    return dict_flag_rules


def apply_alias_rules(dict_flag_rules, alias_rules):
    for alias_rule in alias_rules:
        alias, target = alias_rule[0], alias_rule[2]
        dict_flag_rules[alias] = dict_flag_rules[target]


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

        # element == flag_name
        if element.startswith('-'):
            # Value가 나와야 할 차례
            if turn == "VALUE":
                return False

            # 이미 사용된 flag
            if flag_rules[element] in used_flag.keys():
                return False

            # 존재하지 않는 flag
            if element not in flag_rules.keys():
                return False
            else:
                cur_flag_type = flag_rules[element]
                used_flag[cur_flag_type] = True

                if cur_flag_type != "NULL":
                    turn = "VALUE"

        # element == flag_type
        else:
            # FLAG가 나와야 할 차례
            if turn == "FLAG":
                return False

            if cur_flag_type == "STRING":
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


# a = "line"
# b = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
# c = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]
# solution(a, b, c)
#
# a = "bank"
# b = ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
# c = ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]
# solution(a, b, c)

# # -e 다음 다른 타입
# a = "line"
# b = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
# c = ["line -n 100 -e -s a"]
# solution(a, b, c)

# Strings 타입에 대한 플래그 이후 바로 플래그가 나온 경우
a = "line"
b = ["-s STRING", "-ss STRINGS", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
c = ["line -ss -s hi -e"]
solution(a, b, c)

