from collections import Counter

def cardinalitySort(nums):
    # Write your code here
    nums.sort()
    num_with_one = []
    for num in nums:
        num_with_one.append([num, Counter(str(bin(num))[2:])['1']])

    num_with_one = sorted(num_with_one, key=lambda item: item[1])
    ans = [num[0] for num in num_with_one]
    return ans


nums = [2,3,7,15,31]
nums = [1,2,3,4]
nums = [1,1,4,3,3,2,5]

cardinalitySort(nums)