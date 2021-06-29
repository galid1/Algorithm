import sys
sys.setrecursionlimit(1000000)


# 첫번째 요소를 피벗으로 하여 정렬
# def quick(begin, end):
#     pivot = nums[begin]
#     L, R = begin+1, end
#
#     while L <= R:
#         while L <= end and nums[L] < pivot:
#             L += 1
#         while R > begin and nums[R] > pivot:
#             R -= 1
#
#         if L > R:
#             nums[begin], nums[R] = nums[R], nums[begin]
#         else:
#             nums[L], nums[R] = nums[R], nums[L]
#             L, R = L+1, R-1
#
#     if R > begin:
#         quick(begin, R)
#     if L < end:
#         quick(L, end)


# 중앙값을 피벗으로하여 정렬
def quick(begin, end):
    global nums

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
        quick(L, end)
    if R > begin:
        quick(begin, R)


n = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().strip()))
quick(0, n-1)

for num in nums:
    print(num)

# 5
# 3
# 7
# 1
# 4
# 2

# 5
# 5
# 4
# 3
# 2
# 1


# 7
# 9
# 1
# 6
# 5
# 3
# 2
# 4

# 20
# 9
# 10
# 8
# 7
# 6
# 5
# 2
# 3
# 4
# 1
# 12
# 13
# 15
# 11
# 19
# 18
# 14
# 17
# 16
# 20

#check
# from itertools import permutations
# nums = [1,2,3,4,5,6,7]
#
# ps = list(permutations(nums, 7))
# for p in ps:
#     print(p)
#     p = list(p)
#     quick(p, 0, 6)
#     print('after : ', p)
