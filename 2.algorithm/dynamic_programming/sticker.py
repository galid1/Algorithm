# 백준 9465 스티커
# d[j][i] = i열 까지 고려했을때 j를 선택했을때의 최댓값 (단 해당 스티커를 떼면 상하좌우의 스티커는 사용을 못함)
# 예를 들어 d[0][2] 은 2번째 열까지 고려했을때 2번째 열에서 0을 선택했을 때의 최대값을 구하는 점화식
# d[0][2] = max(d[0][1], d[1][1] + sticker[0][2]) 이된다.
# 즉 d[0][i] = max(d[0][i-1], d[1][i-1] + sticker[0][i]) , d[1][i] = max(d[0][i-1] + sticker[1][i], d[1][i-1])

import sys

def sticker(n, sticker_info):
    d = [[0 for i in range(n)] for i in range(2)]

    # 초기화
    d[0][0] = sticker_info[0][0]
    d[1][0] = sticker_info[1][0]

    # d[j][n] 구하기
    for i in range(1, n):
        d[0][i] = max(d[0][i-1], d[1][i-1] + sticker_info[0][i])
        d[1][i] = max(d[0][i-1] + sticker_info[1][i], d[1][i-1])

    print(max(d[0][n-1], d[1][n-1]))

test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())
    sticker_info = []
    for k in range(2):
        sticker_info.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    sticker(n, sticker_info)
