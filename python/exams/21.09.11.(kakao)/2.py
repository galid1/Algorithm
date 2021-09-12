import math


def solution(n, k):
    answer = 0

    # 문자열로 리턴
    k_prime_n = make_k_prime(k, n)

    idx = 0
    while idx < len(k_prime_n):
        next_idx = idx
        while next_idx < len(k_prime_n) and k_prime_n[next_idx] != '0':
            next_idx += 1

        if next_idx != idx:
            target = k_prime_n[idx:next_idx]
            if is_prime_num(int(target)):
                answer += 1

        idx = next_idx + 1


    return answer


def make_k_prime(k, num):
    result = ''

    while num:
        result = str(num%k) + result
        num //= k

    return result


def is_prime_num(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


# n = 437674
# k = 3
# print(solution(n, k))

n = 110011
k = 10
print(solution(n, k))