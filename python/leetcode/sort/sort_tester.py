import random

def _sort(nums):
    for i in range(len(nums)-1, -1, -1):
        for j in range(0, i):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)
    return nums

nums = [i for i in range(20)]
str_nums = ''.join(list(map(str, nums)))

for _ in range(10):
    random.shuffle(nums)
    res = ''.join(list(map(str, _sort(nums))))
    print(res == str_nums)