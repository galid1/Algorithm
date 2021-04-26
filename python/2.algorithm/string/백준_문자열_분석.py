import sys

# 소문자, 대문자, 숫자, 공백
def solve(s):
    small, big, num, space = 0, 0, 0, 0

    for c in s:
        if c == '\n':
            break

        if c.isdigit():
            num += 1
        elif c == ' ':
            space += 1
        elif c.isalpha():
            if c.isupper():
                big += 1
            else:
                small += 1

    print(small, big, num, space)



while True:
    s = list(sys.stdin.readline())
    if not s:
        exit()

    solve(s)

