# 프로그래머스 주식가격

import sys, collections

def solution(prices):
    answer = [(len(prices) - i - 1) for i in range(len(prices))]

    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
    print(answer)
    return answer


# prices = [1,2,3,2,3]
prices = [5, 1, 2, 3, 1, 7]
# 1 4 2 1 1 0
solution(prices)
