import sys


def solve():
    global ss

    for s in ss:
        is_only = True
        length = len(s)
        # 건너띄기에 사용되는 변수
        for i in range(1, length):
            ds = set()
            for idx, c in enumerate(s):
                if idx+i >= length:
                    break

                pair = c + s[i+idx]
                if pair in ds:
                    is_only = False
                    break
                else:
                    ds.add(pair)

            if not is_only:
                break

        s = ''.join(s)
        if is_only:
            print(s, 'is surprising.')
        else:
            print(s, 'is NOT surprising.')


ss = []
while True:
    s = sys.stdin.readline().strip()
    if s == '*':
        break

    ss.append(list(s))

solve()