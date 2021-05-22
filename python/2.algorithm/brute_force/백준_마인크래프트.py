import sys
# 포인트 !!! : 보드에 나온 수 외의 사이 값들도 높이가 될 수 있다.

def solve():
    global n, m, b, heights, cnts

    ans_sec = sys.maxsize
    ans_height = 0

    for will_height in range(257):
        sec = 0
        highers = 0
        lowers = 0

        for height, cnt in cnts.items():
            diff = height - will_height

            # 현재 만들어야 하는 높이 보다 높음
            if diff > 0:
                highers += diff * cnt
                sec += diff * 2 * cnt

            # 더 낮음
            elif diff < 0:
                lowers += abs(diff) * cnt
                sec += abs(diff) * cnt

            # 같음
            else:
                continue

        if b + highers >= lowers:
            if sec < ans_sec:
                ans_height = will_height
                ans_sec = sec
            elif sec == ans_sec and will_height > ans_height:
                ans_height = will_height
                ans_sec = sec


    print(ans_sec, ans_height)



n, m, b = map(int, sys.stdin.readline().strip().split(" "))
board = []
heights = set()
for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    for num in line:
        heights.add(num)
    board.append(line)

cnts = {}
for num in heights:
    cnts[num] = 0

for i in range(n):
    for j in range(m):
        cnts[board[i][j]] += 1

solve()

# 3 4 99
# 0 0 0 0
# 0 1 2 3
# 0 1 0 0
