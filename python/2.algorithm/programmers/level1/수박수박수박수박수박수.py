def solution(n):
    answer = ''

    answer += '수박' * (n//2)

    if n % 2 != 0:
        answer += '수'

    return answer

# def solution(n):
#     s = '수박' * n
#     return s[:n]


print(solution(1))
solution(2)
print(solution(3))
print(solution(4))