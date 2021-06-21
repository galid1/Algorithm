def solution(S):
    min_length = 201
    for i in range(0, len(S)-1):
        for j in range(i+1, len(S)):
            if check(S[i:j+1]):
                min_length = min(min_length, j-i+1)
                break

    if min_length == 201:
        return -1
    else:
        return min_length


def check(sub_S):
    ss, bs = set(), set()

    for c in sub_S:
        if c.islower():
            ss.add(c)
        else:
            bs.add(c)
    ss, bs = sorted(ss), sorted(bs)

    ss_len, bs_len = len(ss), len(bs)
    if ss_len != bs_len:
        return False

    for i in range(ss_len):
        if ss[i] != bs[i].lower():
            return False

    return True

S = 'AbccaBaC'
print(solution(S))

S = "azABaabza"
print(solution(S))

S = "TacoCat"
print(solution(S))

S = "CATattac"
print(solution(S))

S = "Madam"
print(solution(S))

S = "AcZCbaBz"
print(solution(S))

S = "abcdefghijklmnoq"
print(solution(S))

S = "ABCabcaaBbA"
print(solution(S))
