import sys


def solve():
    global ss, max_len

    answer = ''

    for i in range(len(ss[0])):
        for j in range(5):
            c = ss[j][i]
            if c == ' ':
                continue
            else:
                answer += c

    print(answer)


ss = []
max_len = 0
for _ in range(5):
    s = list(sys.stdin.readline().strip())
    max_len = max(max_len, len(s))
    ss.append(s)

for s in ss:
    diff = max_len - len(s)
    if diff > 0 :
        s += [' '] * diff

solve()