# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)


def solution(n):
    visit = [i for i in range(0, n+1)]
    visit[1] = 0

    # 2 ~ n 까지 (n=10 , 2~ 10)
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i*j > n:
                break
            if visit[j] == 0:
                continue

            visit[i*j] = 0

    answer = 0
    for k in range(2, len(visit)):
        if visit[k] != 0:
            answer += 1

    return answer

solution(10)

