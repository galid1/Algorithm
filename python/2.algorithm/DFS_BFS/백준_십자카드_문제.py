import sys

def find_clock_num(num):
    clock_num = num

    for _ in range(3):
        num = (num % 1000 * 10) + num // 1000

        if clock_num > num:
            clock_num = num

    return clock_num

clock_num = find_clock_num(int(''.join(sys.stdin.readline().strip().split(" "))))

cnt = 0
i = 1111
while i <= clock_num:
    # 현재 i가 clock_num 이라면 cnt + 1
    if find_clock_num(i) == i:
        cnt += 1
    i += 1

print(cnt)