import sys

def solution(n):
    tn = str(n)
    new_num = ''
    cnt = 0

    while True:
        # 2자리 수인 경우 각자리 수를 더함
        if len(tn) >= 2:
            new_num = str(int(tn[0]) + int(tn[1]))
        else:
            new_num = n

        tn = tn[-1] + new_num[-1]

        cnt += 1

        if str(n) == tn:
            break

    print(cnt)


n = int(sys.stdin.readline())
solution(n)