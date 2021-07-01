def twoSum(nums, target):
    index_map = {v:i for i, v in enumerate(nums)}

    for idx, num in enumerate(nums):
        sub = target-num

        if sub in index_map.keys():
            sec_num_idx = index_map[sub]
        else:
            continue

        if idx != sec_num_idx:
            return [idx, index_map[sub]]

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
