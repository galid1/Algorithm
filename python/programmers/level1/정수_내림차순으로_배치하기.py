def solution(n):
    answer = []

    while n:
        answer.append(n%10)
        n //= 10

    answer = list(map(str, sorted(answer, reverse=True)))
    return ''.join(answer)


print(solution(118372))