import random

def _sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        for j in range(i - 1, -2, -1):
            if nums[j] > tmp:
                nums[j + 1] = nums[j]
            else:
                break

        nums[j + 1] = tmp
    return nums

nums = [i for i in range(20)]
str_nums = ''.join(list(map(str, nums)))

for _ in range(10):
    random.shuffle(nums)
    res = ''.join(list(map(str, _sort(nums))))
    print(res == str_nums)
