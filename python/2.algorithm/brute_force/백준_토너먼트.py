import sys


def solution():
    global n, k, l

    matches = [i for i in range(1, n + 1)]
    answer = 0

    # 크기 순으로 정렬
    if k > l:
        k, l = l, k

    while len(matches) > 1:
        is_odd = len(matches) % 2 != 0
        last = n - 1 if is_odd else n

        # round 증가
        answer += 1

        for i in range(0, last, 2):
            # 정답 확인
            if {k, l}.issubset(set([matches[i], matches[i+1]])):
                return answer

        # k , l 최신화
        k, l = (k+1)//2, (l+1)//2

        if is_odd:
            n += 1
        n //= 2
        matches = [i for i in range(1, n + 1)]


    print(-1)


n, k, l = map(int, sys.stdin.readline().strip().split(" "))
print(solution())