# KMP
# 특정 '문자열' 내의 특정 '패턴'을 빠르게 찾을 때 사용하는 알고리즘,
# 패턴의 부분 문자열만큼 일치한다는 정보를 이용하여 검사 위치를 건너 띄어 효율적으로 검사하는 방법이다.
# m: 일치 문자열 길이
# p[]: 접두, 접미사 일치 길이 배열 ( 패턴내의 반복되는 문자열 검사를 건너띄지 않기 위해 사용 )
# 문자열의 특정 위치에서 패턴 일치를 검사한다, 불일치하는 경우 일치하는 만큼 건너띄고, 패턴내의 반복되는 문자열만큼 되돌아와서 검사한다.

import sys


def solve():
    global s, p

    ps = make_ps()


def make_ps():
    # abcabc
    # ababa
    p = "ababa"
    ps = [0 for _ in range(len(p))]

    h, t = 0, 1
    while t < len(p):
        if p[h] == p[t]:
            h, t = h+1, t+1
            ps[t] = h

        else:
            h, t = 0, t+1

    print(ps)

def make_skip_table():
    pat = 'ababa'
    skips = [0 for _ in range(len(pat) + 1)]
    pp = 0
    pt = 1
    while pt < len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skips[pt] = pp
        elif pp == 0:
            pt += 1
            skips[pt] = pp
        else:
            pp = skips[pp]

    return skips


# s = sys.stdin.readline().strip()
# p = sys.stdin.readline().strip()

solve()