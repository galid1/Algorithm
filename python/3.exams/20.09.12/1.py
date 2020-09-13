import sys, re


def to_lowwer(str):
    return str.lower()

# print(to_lowwer("asnd-TTASDla@@!@#$"))
# print(to_lowwer(''))


def remove_symbol(str):
    return re.sub('[^\.\-\_A-Za-z0-9]+', '', str)

# print(remove_symbol('z-+.^.'))
# print(remove_symbol('1234567890-_=+~!@#$//?<>asdfwerquiopzxcvbnm,afdhj....kl'))
# print(remove_symbol(''))


def remove_repetitive_dot(str):
    str_arr = list(str)
    new_str = str_arr[0]

    for i in range(1, len(str_arr)):
        c = str_arr[i]

        if c != '.':
            new_str += c
            continue

        if c == '.' and new_str[-1] != '.':
            new_str += c

    return new_str

# print(remove_repeative_dot("..aaaa...."))
# print('')
# print(remove_repetitive_dot('z-..'))


def remove_start_end_dot(str):
    if not str:
        return str

    if str[0] != '.' and str[-1] != '.':
        return str

    if str[0] == '.':
        return remove_start_end_dot(str[1:])

    if str[-1] == '.':
        return remove_start_end_dot(str[:-1])

# print(remove_start_end_dot(".aaa..abbb.."))
# print('')
# print(remove_start_end_dot('z-..'))


def if_empty_str(str):
    new_str = str.strip()

    if not new_str:
        new_str += 'a'

    return new_str


# print(if_empty_str('    '))


def limit_length(str):
    limit = 15
    new_str = (str[:limit])
    return remove_start_end_dot(new_str)


# print(limit_length('12345678901234.67'))


def to_over_three(str):
    new_str = str
    while len(new_str) <= 2:
        new_str += new_str[-1]

    return new_str


# print(to_over_three('a'))
# print(to_over_three('z-'))



def solution(new_id):
    answer = to_lowwer(new_id)
    answer = remove_symbol(answer)
    answer = remove_repetitive_dot(answer)
    answer = remove_start_end_dot(answer)
    answer = if_empty_str(answer)
    answer = limit_length(answer)
    answer = to_over_three(answer)

    return answer
