def solution(x, n):
    answer = []

    adder = x
    for i in range(n):
        answer.append(x)
        x += adder

    return answer

solution(2, 5)