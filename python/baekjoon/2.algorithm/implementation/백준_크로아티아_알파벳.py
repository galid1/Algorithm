import sys


def solve():
    global s

    ans = 0
    idx = 0
    while idx < len(s) - 1:
        if s[idx] not in cs.keys():
            idx += 1
            ans += 1

        # 일단 첫 글자가 크로아티아 글자에 존재하는 상태
        else:
            if s[idx+1] in cs[s[idx]]:
                # z인 경우 별도 처리 필요
                if s[idx+1] == 'z':
                    if idx + 2 < len(s) and s[idx+2] == '=':
                        idx += 3
                        ans += 1
                    else:
                        idx += 1
                        ans += 1
                        continue
                else:
                    idx += 2
                    ans += 1
            else:
                idx += 1
                ans += 1

    if idx < len(s):
        ans += 1
    print(ans)

cs = {
    "c": ['=', '-'],
    "d": ['z', '-'],  # z는 = 가 추가적으로 있는지 확인 필요
    "l": ['j'],
    "n": ['j'],
    "s": ['='],
    "z": ['=']
}

s = list(sys.stdin.readline().strip())
solve()
