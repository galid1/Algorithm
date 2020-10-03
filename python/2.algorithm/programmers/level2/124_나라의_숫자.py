# 0. 몫이 3보다 클 때까지만 아래 반복
# 1. 3으로 나눔
# 2. 나머지를 문자열 맨앞에 더함
# 3. 나머지가 0인 경우 4로 바꾸어 더함, 몫에서 1을 뺌

def solution(n):
    answer = ''

    while n > 0:
        remainder = str(n%3)
        n //= 3

        if remainder == '0':
            remainder = '4'
            n -= 1

        answer = remainder + answer

    return answer


solution(1)
solution(2)
solution(3)
solution(4)
solution(10)
solution(11)
solution(12)
solution(13)