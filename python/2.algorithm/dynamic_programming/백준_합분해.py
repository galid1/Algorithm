import sys

def solve():
    global n, k

    # d[k][n] == k개의 정수를 사용하여, n을 만드는 경우의 수
    d = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        d[1][i] = 1

    # j == 사용할 정수 개수 (2개 사용부터)
    for j in range(2, k+1):
        # h == 만들 정수 (0부터 , 0도 사용가능 하기 때문)
        for h in range(0, n+1):
            for g in range(h+1):
                d[j][h] += d[j-1][g]

    print(d[k][n]%1000000000)


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()