import sys


def solve():
    global n, m, a, b

    quick_sort(a, 0, n-1)
    quick_sort(b, 0, m-1)

    # 투포인트 정렬 (각 배열이 정렬되어 있다는 가정)
    if n > m:
        n, m = m, n
        a, b = b, a

    new_s = []
    a_p, b_p = 0, 0
    while a_p < n and b_p < m:
        if a[a_p] < b[b_p]:
            new_s.append(a[a_p])
            a_p += 1
        else:
            new_s.append(b[b_p])
            b_p += 1

    while a_p < n:
        new_s.append(a[a_p])
        a_p += 1
    while b_p < m:
        new_s.append(b[b_p])
        b_p += 1


    for n in new_s:
        print(n, end=' ')


def quick_sort(nums, begin, end):
    pivot = nums[(begin+end)//2]
    L, R = begin, end

    while L <= R:
        while nums[L] < pivot:
            L += 1
        while nums[R] > pivot:
            R -= 1

        if L <= R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L+1, R-1

    if L < end:
        quick_sort(nums, L, end)
    if R > begin:
        quick_sort(nums, begin, R)


n, m = map(int, sys.stdin.readline().strip().split(" "))
a = list(map(int, sys.stdin.readline().strip().split(" ")))
b = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()


# 3 4
# 4 1 9
# 2 10 7 5