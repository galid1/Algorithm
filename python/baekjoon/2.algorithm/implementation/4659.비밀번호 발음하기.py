import sys


def solve(word):
    print_ans(word, decide_acceptable(word))


def decide_acceptable(word):
    bef = ""
    bef_type = ""
    vowel_cnt = 0
    continuous_cnt = 1

    for c in word:
        c_type = get_type(c)

        if c_type == bef_type:
            continuous_cnt += 1
        else:
            continuous_cnt = 1

        # 모음 또는 자음 3번이상 안됌
        if continuous_cnt >= 3:
            return False

        # 같은 글자 판단
        if bef == c and c != "e" and c != "o":
            return False

        # 후처리 (모음 수 증가, 이전 글자 갱신)
        if c_type == "VOWEL":
            vowel_cnt += 1
        bef, bef_type = c, c_type

    if vowel_cnt < 1:
        return False
    return True


def get_type(c):
    if c in ["a", "i", "o", "u", "e"]:
        return "VOWEL"
    return "CONSONANT"


def print_ans(word, is_right=True):
    template = "is acceptable."
    if not is_right:
        template = "is not acceptable."

    print("<" + word + ">" , template)


while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break
    solve(word)


# get type test
# for num in range(97, 97+26):
#     print("========")
#     print("cur c ", chr(num))
#     print(get_type(chr(num)))

# aab
# c
# i

# caccac
# abeecoo


# 같은 타입 3번 테스트
# aei
# aie
# oui
# euo
# end

# eeo
# eei
# ooe
# ooi
# eie
# oio
# eee
# ooo
# end


# 같은 글자 두번 테스트
# aa
# bb
# cc
# dd
# ee
# ff
# gg
# hh
# ii
# jj
# kk
# oo
# uu
# end
