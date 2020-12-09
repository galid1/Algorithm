import sys


def solution():
    answer = 0
    for num in range(123, 987 + 1):
        num = str(num)
        if '0' in num:
            continue
        if is_dup(num):
            continue

        if check_possibility(num):
            answer += 1

    print(answer)

def is_dup(num):
    for i in range(2):
        for j in range(i+1, 3):
            if i == j:
                continue
            if num[i] == num[j]:
                return True

    return False

def check_possibility(num):
    global ans

    for a in ans:
        cur_num = str(a[0])
        tmp_s = a[1]
        tmp_b = a[2]

        if tmp_s == 0 and tmp_b == 0:
            for i in range(3):
                if cur_num[i] in num:
                    return False

        s, b = 0, 0
        for i in range(3):
            for j in range(3):
                if i == j:
                    if cur_num[i] == num[j]:
                        s += 1
                elif i != j:
                    if cur_num[i] == num[j]:
                        b += 1

        if tmp_s != s or tmp_b != b:
            return False

    return True


n = int(sys.stdin.readline())
ans = []
for i in range(n):
    ans.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solution()