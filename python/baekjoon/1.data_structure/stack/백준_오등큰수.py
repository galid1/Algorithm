import sys


def solve():
    global n, nums

    # cnts 기록
    cnts = get_cnts()

    stack = []
    for i in range(len(nums)):
        # stack이 빈 경우
        if not stack:
            stack.append(i)
            continue

        #  f(ni)가 스택 상단의 f(ai) 보다 작거나 같은 경우
        if cnts[nums[stack[-1]]] >= cnts[nums[i]]:
            stack.append(i)
            continue

        # f(ni)가 더 큰 경우
        while stack and cnts[nums[stack[-1]]] < cnts[nums[i]]:
            idx = stack.pop()
            nums[idx] = nums[i]
        stack.append(i)

    # stack에 남은 친구들 모두 -1로
    while stack:
        idx = stack.pop()
        nums[idx] = -1

    # 정답
    for num in nums:
        print(num, end=' ')


def get_cnts():
    global n, nums

    cnts = {}

    for num in nums:
        if num not in cnts.keys():
            cnts[num] = 1
        else:
            cnts[num] += 1

    return cnts



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()