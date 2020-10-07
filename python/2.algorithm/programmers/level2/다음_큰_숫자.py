from collections import Counter

# 1의 개수를 직접 세며 비교
def solution(n):
    one_cnt = Counter(bin(n)).get('1')

    next = n + 1
    while True:
        next_one_cnt = Counter(bin(next)).get('1')

        if one_cnt == next_one_cnt:
            return next

        next += 1

print(solution(78))

