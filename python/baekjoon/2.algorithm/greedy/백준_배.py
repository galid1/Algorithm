import sys

def solve():
    global n, m, cs, bs

    # 불가능
    if bs[0] > cs[1]:
        return print(-1)

    ans = 0
    while bs:
        ans += 1

        # 크레인 쎈 것 부터
        for i in range(1, n+1):
            # 박스 순회
            for j in range(len(bs)):
                # 옮기기
                if cs[i] >= bs[j]:
                    del bs[j]
                    break

    print(ans)


n = int(sys.stdin.readline().strip())
cs = list(map(int, sys.stdin.readline().strip().split(" ")))
cs.sort(reverse=True)
cs = [0] + cs

m = int(sys.stdin.readline().strip())
bs = list(map(int, sys.stdin.readline().strip().split(" ")))
bs.sort(reverse=True)
solve()

# 3
# 6 8 9
# 7
# 9 9 8 7 7 6 5

# 3
# 6 6 7
# 10
# 1 5 7 6 2 7 6 5 2 3

# 3
# 1 2 3
# 10
# 1 1 1 1 2 2 2 3 3 3