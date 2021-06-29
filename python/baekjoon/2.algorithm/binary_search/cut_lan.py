# baekjoon 1654 랜선 자르기

import sys


def solution(k, lans):
    # 여기에 저장된 값들중 가장 큰 값이 정답
    cut_lens= []

    start_len = 1
    end_len = 2147483647
    cut_len = 0

    while end_len >= start_len:
        cut_len = (start_len + end_len)//2

        # 자르려는 길이로 각각의 랜선을 자르며 총 개수를 구함(그전에 초기화)
        lan_count = 0
        for lan in lans:
            lan_count += lan//cut_len

        if lan_count >= k:
            cut_lens.append(cut_len)
            start_len = cut_len + 1
        else:
            end_len = cut_len - 1

    print(max(cut_lens))


n, k = map(int, sys.stdin.readline().rstrip().split(" "))
lans = []
for i in range(n):
    lans.append(int(sys.stdin.readline()))
solution(k, lans)