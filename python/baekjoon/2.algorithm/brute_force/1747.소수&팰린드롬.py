# import sys, math
#
#
# def solve():
#     global n
#
#     while True:
#         if find(n):
#             break
#         n += 1
#
#     print(n)
#
#
# def find(num):
#     num_str = str(num)
#
#     if num < 2:
#         return False
#
#     for i in range(len(num_str)//2):
#         if num_str[i] != num_str[len(num_str)-1-i]:
#             return False
#
#     for i in range(2, int(math.sqrt(num))+1):
#         if num%i == 0:
#             return False
#
#     return True
#
#
# n = int(sys.stdin.readline().strip())
# solve()

import sys


def solve():
    global n

    arr = init()
    ans = -1

    for num in range(n, len(arr)):
        if not arr[num]:
            continue

        if palindrome(num):
            ans = num
            break

    print(ans)


def palindrome(num):
    str_num = str(num)

    for i in range(len(str_num)//2):
        if str_num[i] != str_num[len(str_num)-1-i]:
            return False
    return True


def init():
    arr = [True for _ in range(1004000)]
    arr[0] = False
    arr[1] = False

    for i in range(2, 1000400):
        if arr[i]:
            for j in range(i*2, len(arr), i):
                arr[j] = False

    return arr


n = int(sys.stdin.readline().strip())
solve()