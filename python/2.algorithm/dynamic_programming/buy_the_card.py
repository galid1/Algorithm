# 백준 11052 카드 구매하기

import sys
import collections

def card_num(n, p):
    d = [0 for i in range(1001)]

    d[1] = p[1]

    # d[n] (최대 금액)을 구하기위한 반복문
    for i in range(2, n+1):
        # 각 d[i]마다 최대금액을 구하기 위한 반복문
        for j in range(1, i+1):
            d[i] = max(d[i], p[j] + d[i-j])

    print(d[n])

n = int(sys.stdin.readline())
# prices를 보기 편하게 일부러 인덱스를 한칸 뒤로 밈
prices = collections.deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
prices.appendleft(0)
card_num(n, prices)
