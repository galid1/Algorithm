def greedy_atm(nums):
    sum = 0
    for i in range(0, len(nums)):
        for j in range(0, i + 1):
            sum += nums[j]
    return sum

def sort(nums):
    for i in range(0, len(nums)-1):
        min = i
        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                min = j
        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp

if __name__ == "__main__":
    people_num = input()
    withdraw_time_str = input().split(" ")
    withdraw_time = list(map(int, withdraw_time_str))
    sort(withdraw_time)
    print(greedy_atm(withdraw_time))