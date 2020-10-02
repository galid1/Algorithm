def solution(num):
    answer = 0

    while num != 1:
        answer += 1

        if num % 2 == 0:
            num //=2
        else:
            num *= 3
            num += 1

        if answer >= 500:
            return -1

    return answer

solution(1)
solution(6)
solution(16)
solution(626331)