def solution(phone_number):
    answer = ''

    start = len(phone_number) - 4
    end = len(phone_number) + 1
    answer = ('*' * (start - 0) + phone_number[start: end])

    return answer