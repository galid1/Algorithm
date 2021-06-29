import sys

# 1, 2로 4를 만든는 방법 = 2가지
# 2를 사용하지 않는 경우 => 1로만 만드는 경우 == D[n-1, k]
# 2를 사용하는 경우 => 4-2를 1,2로 만드는 경우에 2를 추가 == D[n, k-2]

def solution(n, k, cs):
    d = [[0 for _ in range(k+1)] for _ in range(3)]
    d[0][0] = 1

    for i in range(1, n+1):
        for j in range(0, k+1):
            d[1][j] = d[0][j]

            if j - cs[i-1] >= 0:
                d[1][j] += d[1][j-cs[i-1]]

        d[0] = d[1]

    print(d[1][k])

n, k = map(int, sys.stdin.readline().strip().split(" "))
cs = []
for i in range(n):
    cs.append(int(sys.stdin.readline()))
solution(n, k, cs)
