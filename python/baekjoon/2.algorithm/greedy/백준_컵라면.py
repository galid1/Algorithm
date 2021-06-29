import sys
# n = 3 일때
# 1 3
# 2 4
# 2 5
# 위와 같이 정보가 주어지면, 1은 선택안하고, 2 두개를 선택하는게 이득

# n = 3 일때
# 3 5
# 3 4
# 1 1
# 이 경우, 모두 선택이 가능하지만 잘 짜야함

def solve():
    global n, infos

    # 1초부터 사용
    ans = [0 for _ in range(n + 1)]

    # 포인트(각 데드라인의 마지막 지점을 저장하는 맵)
    ds = {d:d for d in range(1, n+1)}

    for d, num in infos:
        for t in range(ds[d], 0, -1):
            # 아직 사용되지 않은 시간의 경우
            if ans[t] == 0:
                ans[t] = num
                ds[d] -= 1
                break

    print(sum(ans))


n = int(sys.stdin.readline().strip())
infos = []
for _ in range(n):
    d, num = map(int, sys.stdin.readline().strip().split(" "))
    infos.append((d, num))

infos = sorted(infos, key=lambda i: i[1], reverse=True)
solve()

# 6
# 5 9
# 4 7
# 5 6
# 5 8
# 4 9
# 3 2
# => 39

# 3
# 1 3
# 2 4
# 2 5
# => 9

# 3
# 3 5
# 3 4
# 1 1
# => 10

# 7
# 1 6
# 1 7
# 3 2
# 3 1
# 2 4
# 2 5
# 6 1