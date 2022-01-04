# KMP
# 특정 '문자열' 내의 특정 '패턴'을 빠르게 찾을 때 사용하는 알고리즘,
# 패턴의 부분 문자열만큼 일치한다는 정보를 이용하여 검사 위치를 건너 띄어 효율적으로 검사하는 방법이다.
# m: 일치 문자열 길이
# p[]: 접두, 접미사 일치 길이 배열 ( 패턴내의 반복되는 문자열 검사를 건너띄지 않기 위해 사용 )
# 문자열의 특정 위치에서 패턴 일치를 검사한다, 불일치하는 경우 일치하는 만큼 건너띄고, 패턴내의 반복되는 문자열만큼 되돌아와서 검사한다.

import sys

def kmp_match(txt: str, pat: str) -> int:
    # 스킵테이블 만들기
    def make_skip_table(skip: list):
        pt = 1  # txt를 따라가는 인덱스
        pp = 0  # pat를 따라가는 인덱스
        while pt < len(pat):
            if pat[pt] == pat[pp]:
                pt += 1
                pp += 1
                skip[pt] = pp
            elif pp == 0:
                pt += 1
                skip[pt] = pp
            else:
                pp = skip[pp]

    # 부분 문자열 찾기 (이 문제에서는 있는지 없는지만 찾으면 된다.)
    def find_match_idx(txt: str, pat: str) -> int:
        pt = 0
        pp = 0
        while pt < len(txt) and pp < len(pat):
            if txt[pt] == pat[pp]:
                pt += 1
                pp += 1
            elif pp == 0:  # 더 이상 앞으로 돌아갈 수 없는 경우
                pt += 1
            else:
                pp = skip[pp]
        if pp == len(pat):
            return 1
        else:
            return 0

    skip = [0] * (len(pat) + 1)
    make_skip_table(skip)
    answer = find_match_idx(txt, pat)
    print(answer)


if __name__ == '__main__':
    S = input()
    P = input()
    kmp_match(S, P)