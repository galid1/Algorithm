def solution(num):
    answer = True

    total = 0
    t_num = num

    while t_num:
        total += t_num % 10
        t_num //= 10

    if num % total != 0:
        answer = False

    return answer


solution(10)
solution(12)
solution(11)
solution(13)