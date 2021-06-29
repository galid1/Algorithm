import sys

def solve():
    global s, w

    ls, lw = len(s), len(w)
    i = 0
    ans = 0
    while i <= ls - lw:
        if s[i: i+lw] == w:
            ans += 1
            i += lw
            continue

        # 다음 인덱스
        i += 1

    print(ans)

s = list(sys.stdin.readline().strip())
w = list(sys.stdin.readline().strip())
solve()

# ababababa
# aba