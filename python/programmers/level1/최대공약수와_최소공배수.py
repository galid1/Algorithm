def solution(n, m):
    answer = [0, 0]

    # 큰 수를 뒤로
    if n > m:
        n, m = m, n

    for i in range(n, 0, -1):
        if n%i == 0 and m%i == 0:
            answer[0] = i
            break

    j = 1
    while True:
        tm = m * j

        if tm % n == 0:
            answer[1] = tm
            break

        j += 1

    return answer

solution(15, 20)
solution(3, 12)
solution(2, 5)