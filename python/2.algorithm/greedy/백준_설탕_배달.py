import sys

def solution(n):
    cnt = 0

    while True:
        if n % 5 == 0:
            cnt += n//5
            print(cnt)
            return

        n -= 3
        cnt += 1

        if n < 0:
            print(-1)
            return


n = int(sys.stdin.readline())
solution(n)