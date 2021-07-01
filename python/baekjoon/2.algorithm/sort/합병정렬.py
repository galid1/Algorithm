import sys

def merge_sort(nums, begin, end, mid):
    if begin == end:
        return [nums[begin]]

    a, b = '', ''
    if begin < end:
        a = merge_sort(nums, begin, mid, (mid+begin)//2)
        b = merge_sort(nums, mid+1, end, (mid+1+end)//2)

    new_list = []
    L, R = 0, 0
    # L => begin -> mid까지 , R은 mid+1 -> end 까지
    while L < len(a) and R < len(b):
        if a[L] <= b[R]:
            new_list.append(a[L])
            L += 1
        else:
            new_list.append(b[R])
            R += 1

    while L < len(a):
        new_list.append(a[L])
        L += 1
    while R < len(b):
        new_list.append(b[R])
        R += 1

    return new_list


n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))
nums = merge_sort(nums, 0, n-1, (n-1)//2)

for num in nums:
    print(num)

