def solution(amountText):
    if not compose_only_valid(amountText):
        return False

    if start_zero_and_not_zero(amountText):
        return False

    if not begin_end_is_num(amountText):
        return False

    if has_split_c(amountText) and not right_split(amountText):
        return False

    return True


def compose_only_valid(amountText):
    for c in amountText:
        if not c.isnumeric() and c != ',':
            return False

    return True

def start_zero_and_not_zero(amountText):
    return len(amountText) > 1 and amountText[0] == '0'


def begin_end_is_num(amountText):
    return amountText[0].isnumeric() and amountText[-1].isnumeric()


def has_split_c(amountText):
    for c in amountText:
        if c == ',':
            return True

    return False


def right_split(amountText):
    texts = list(amountText)

    while texts:
        # 3개의 수 제거
        for _ in range(3):
            if not texts:
                break

            if not texts.pop().isnumeric():
                return False

        if texts and texts.pop() != ',':
            return False

    return True

# f0 = "a0"
# f1 = ",c"
# s1 = "0,"
# s2 = ",0"
# s3 = ","
# print(solution(f0))
# print(solution(f1))
# print(solution(s1))
# print(solution(s2))
# print(solution(s3))


# f1 = '00'
# s1 = '0'
# print(solution(f1))
# print(solution(s1))
#
# f2 = ',1'
# s2 = '1'
# f3 = '1,'
# print(solution(f2))
# print(solution(s2))
# print(solution(f3))

print(solution("111,222"))
print(solution("111"))
print(solution(',11'))
print(solution("111,"))
print(solution(",111"))
print(solution("1,000"))