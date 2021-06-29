import sys

def solution():
    global a, b, c, x, y

    # 그냥 각각 구매
    ans = a*x + b*y

    # 반반을 이용한 구매(구매 가능한 만큼만)
    half_ans = min(x, y) * c * 2
    sub = x - y
    if sub > 0:
        half_ans += sub * a
    elif sub < 0:
        half_ans += abs(sub) * b

    ans = min(ans, half_ans)

    # 반반을 이용한 구매(초과 구매)
    half_ans = max(x, y) * c * 2
    ans = min(ans, half_ans)

    print(ans)


a, b, c, x, y = map(int, sys.stdin.readline().strip().split(" "))
solution()