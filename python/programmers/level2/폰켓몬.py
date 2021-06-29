def solution(nums):
    nums.sort()

    can_choice_cnt = len(nums)//2
    choose = [nums[0]]
    for i in range(1, len(nums)):
        if len(choose) >= can_choice_cnt:
            break

        if choose[-1] != nums[i]:
            choose.append(nums[i])

    return len(choose)

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])