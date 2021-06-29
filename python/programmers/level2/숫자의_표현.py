def solution(n):
    answer = 0

    for i in range(1, n+1):
        sums = 0
        for j in range(i, n+1):
            sums += j

            if sums == n:
                answer += 1
                break

            if sums > n:
                break

    print(answer)
    return answer

solution(14)
solution(15)
solution(6)