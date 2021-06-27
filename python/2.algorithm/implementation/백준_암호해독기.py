import sys


def solve():
    global n, enc, dec

    enc_cs = {}
    for i in range(65, 65 + 26):
        enc_cs[chr(i)] = 0
    for i in range(97, 97 + 26):
        enc_cs[chr(i)] = 0
    enc_cs[' '] = 0

    for ec in enc:
        if ec == 0:
            enc_cs[' '] += 1

        elif ec < 27:
            enc_cs[chr(64+ec)] += 1

        else:
            enc_cs[chr(70+ec)] += 1

    for dc in dec:
        if enc_cs[dc] - 1 < 0:
            return print("n")
        else:
            enc_cs[dc] -= 1

    print("y")


n = int(sys.stdin.readline().strip())
enc = list(map(int, sys.stdin.readline().strip().split(" ")))
dec = list(sys.stdin.readline().strip())
solve()
# 11
# 44 0 38 41 38 31 23 8 41 30 38
# Hello  World

# 2
# 52 26
# Zz

# 3
# 1 1 1
# aa

# # 1 ~ 26 : A-Z +64
# # 27 - 52 : a-z +70
# print(chr(27+70))
# print(ord('A')) 97
# print(ord('a')) 65