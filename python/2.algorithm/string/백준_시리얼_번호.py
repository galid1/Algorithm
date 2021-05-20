import sys

# 1. 짧은것 먼저
# 2. 숫자만 확인해서 더한 값이 가장 작은 것
# 3. 사전순
def solve():
    global n, ss

    ss.sort(key=lambda string: string[2])
    ss.sort(key=lambda string: string[0])
    ss.sort(key=lambda string: string[1])

    for s in ss:
        print(s[2])


n = int(sys.stdin.readline().strip())
ss = []

for _ in range(n):
    s = sys.stdin.readline().strip()
    sums = 0
    length = 0
    for c in s:
        length += 1
        if c.isdigit():
            sums += int(c)

    ss.append((sums, length, s))

solve()
