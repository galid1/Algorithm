def solution(N):
    is_neg = N < 0
    sN = str(N).split("-")

    if is_neg:
        sN = sN[1]
        max_N = -int('5' + sN)
        max_N = max(max_N, -int(sN + '5'))

        for i in range(len(sN)+1):
            max_N = max(max_N, -int(sN[:i] + '5' + sN[i:]))
    else:
        sN = sN[0]
        max_N = int('5'+sN)
        max_N = max(max_N, int(sN+'5'))

        for i in range(len(sN)+1):
            max_N = max(max_N, int(sN[:i] + '5' + sN[i:]))

    print(max_N)
    return max_N

N = 268
solution(N)
N = 670
solution(N)
N = 0
solution(N)
N = -999
solution(N)

# for i in range(-8000, 8001):
#     print(i, ": " , end = ' ')
#     print(solution(i))