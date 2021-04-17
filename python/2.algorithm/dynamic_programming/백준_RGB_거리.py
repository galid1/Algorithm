import sys

def solve():
    global n, rgbs

    # r ,g ,b 선
    d = [0 for _ in range(n+1)]
    selected = [0 for _ in range(n+1)]
    d[0] = 0

    # 미리 첫번째, 두번째 작은 수와, 그 idx를 구해 놓는다.

    for i in range(1, n+1):
        # 현재 rgb에서 제일 작은 값을 일단 찾는다.
        min_rgb = 1001
        min_idx = -1
        for j in range(3):
            min_rgb = min(min_rgb, rgbs[i][j])
            min_idx = j

        # 현재 선택한 rgb가 이전 rgb와 같으면, 이전 rgb를 모두 최신화 한 것과,
        # 현재를 그냥 그다음 작은 값의 idx로 바꾼것 중 더 작은 것으로 선택
        tmp_rgb_sum = min_rgb
        if selected[i-1] == min_idx:
            # i부터 0까지 최신화
            for k in range(i-1, 0, -1):

        if



n = int(sys.stdin.readline().strip())
rgbs = []
for i in range(n):
    rgbs.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()