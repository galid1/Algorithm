import math

def solution(n):
    n_sqrt = math.sqrt(n)

    if n_sqrt == int(n_sqrt):
        return int(math.pow(n_sqrt + 1, 2))
    else:
        return -1

print(solution(121))
print(solution(3))