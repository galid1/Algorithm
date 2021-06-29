import sys

# elif  R == n 이 중간에 없는 경우 아래와 같은 경우를 처리 하지 못함
# 5 17
# 5 1 2 3 7
# 끝까지 더하고 난 다음 R은 이미 N의 크기와 동일 하기 때문에, L이 증가하며 줄어드는 경우를 체크하지 못함

def solution():
    global n, m, a

    cnt = 0
    L, R = 0, 0

    s = 0
    while True:
        if s >= m:
            s -= a[L]
            L += 1
        elif R == n:
            break
        else:
            s += a[R]
            R += 1

        if s == m:
            cnt += 1

    print(cnt)


n, m = map(int, sys.stdin.readline().strip().split(" "))
a = list(map(int, sys.stdin.readline().strip().split(" ")))
solution()
