import sys

# 가지고 있다가 떨어질 때 팔면, 뒤에 있을 더 높은 주가가 올 때 파는것에 대한 이익을 챙기지 못한다.


def solve():
    global n, stocks

    standard_idx = n-1
    holdings = []
    ans = 0
    idx = standard_idx - 1
    while standard_idx > 0:
        while True:
            # idx가 끝났거나, 현재 기준보다 더 비싼 주가가 나타난 경우
            if idx < 0 or stocks[idx] > stocks[standard_idx]:
                ans += sell_all(stocks[standard_idx], holdings)
                holdings = []
                standard_idx = idx
                break

            holdings.append(stocks[idx])
            idx -= 1

    print(ans)


def sell_all(stock_price, holdings):
    if not holdings:
        return 0

    res = 0
    for holding in holdings:
        res += stock_price - holding
    return res



t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    stocks = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()

# 1
# 9
# 10 7 6 3 5 9 8 2 4

# 1
# 8
# 1 1 2 3 3 2 4 6

# 1
# 7
# 1 1 2 2 3 3 4

# 1
# 8
# 4 1 2 4 5 6 2 2
# => 14