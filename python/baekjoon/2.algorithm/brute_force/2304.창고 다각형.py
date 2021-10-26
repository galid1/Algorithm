import sys


def solve():
    global n, ps

    # 기둥 배치
    length = ps[-1][0] + 1
    polls = [0 for _ in range(length)]
    for x, h in ps:
        polls[x] = h

    # 최대 기둥 높이와 인덱스 찾기
    max_poll_height = 0
    max_poll_idx = 0
    for x, h in ps:
        if h >= max_poll_height:
            max_poll_height = h
            max_poll_idx = x

    ans = max_poll_height
    # 인덱스를 기준으로 좌우 순회
    l_mh = 0
    for i in range(max_poll_idx):
        l_mh = max(l_mh, polls[i])
        ans += l_mh

    r_mh = 0
    for i in range(length-1, max_poll_idx, -1):
        r_mh = max(r_mh, polls[i])
        ans += r_mh

    print(ans)



n = int(sys.stdin.readline().strip())
ps = []
for _ in range(n):
    ps.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ps.sort()
solve()