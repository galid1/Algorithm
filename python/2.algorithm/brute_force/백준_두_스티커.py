import sys

def solve(cur, idx):
    global h, w, n, stickers, ans

    if len(cur) == 2:
        if can_stick(cur, h, w):
            ans = max(ans, cal_area(cur))
        return

    for i in range(idx, n):
        cur.append(stickers[i])
        solve(cur, i+1)
        cur.pop()


def cal_area(stickers):
    area = 0
    for sticker in stickers:
        area += sticker[0] * sticker[1]
    return area


def can_stick(stickers, h, w):
    for i in range(2):
        for j in range(2):
            fir_w, fir_h, sec_w, sec_h = stickers[0][0], stickers[0][1], stickers[1][0], stickers[1][1]
            if i:
                fir_w, fir_h = fir_h, fir_w
            if j:
                sec_w, sec_h = sec_h, sec_w

            # 양 옆 배치
            sh = max(fir_h, sec_h)
            sw = fir_w + sec_w
            if w >= sw and h >= sh:
                return True

            # 위 아래 배치
            sw = max(fir_w, sec_w)
            sh = fir_h + sec_h
            if w >= sw and h >= sh:
                return True

    return False


# 입력
h, w = map(int, sys.stdin.readline().strip().split(" "))
n = int(sys.stdin.readline())
stickers = []
for i in range(n):
    stickers.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))

# 수행 및 결과
ans = 0
solve([], 0)
print(ans)
