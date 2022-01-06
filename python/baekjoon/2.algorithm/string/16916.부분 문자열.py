# KMP
# 특정 '문자열' 내의 특정 '패턴'을 빠르게 찾을 때 사용하는 알고리즘,
# 패턴의 부분 문자열만큼 일치한다는 정보를 이용하여 검사 위치를 건너 띄어 효율적으로 검사하는 방법이다.
# m: 일치 문자열 길이
# p[]: 접두, 접미사 일치 길이 배열 ( 패턴내의 반복되는 문자열 검사를 건너띄지 않기 위해 사용 )
# 문자열의 특정 위치에서 패턴 일치를 검사한다, 불일치하는 경우 일치하는 만큼 건너띄고, 패턴내의 반복되는 문자열만큼 되돌아와서 검사한다.

import sys


def solve():
    global s, p

    ps = make_ps(p)

    idx, jdx = 0, 0
    while idx + len(p) <= len(s):
        same = True
        while jdx < len(p):
            if s[idx + jdx] != p[jdx]:
                same = False
                break
            jdx += 1

        if same:
            return print(1)

        if jdx == 0:
            idx += 1
        else:
            idx += jdx - ps[jdx - 1]
            jdx = ps[jdx - 1]

    print(0)


def make_ps(p):
    ps = [0 for _ in range(len(p))]

    h = 0
    for t in range(1, len(p)):
        while h > 0 and p[h] != p[t]:
            h = ps[h-1]

        if p[h] == p[t]:
            h += 1
            ps[t] = h

    return ps

# a b a c a a b a c a a c d
# 0 0 1 0 1 1 2 3 4 5 6


s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

solve()

# ababcababa
# ababa