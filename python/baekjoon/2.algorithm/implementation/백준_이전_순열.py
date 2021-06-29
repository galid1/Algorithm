import sys


def solve():
    global n, nums

    # nums[k] > nums[k+1] 을 만족하는 가장 큰 k 구하기
    k = -1
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            k = i

    if k == -1:
        return print(-1)

    m = k+1
    for i in range(k+1, n):
        # k번째 수보다 작고 가장 큰 수 찾기
        if nums[k] > nums[i] > nums[m]:
            m = i

    # 수 위치 변경
    nums[k], nums[m] = nums[m], nums[k]

    # m이후 수를 모두 역순으로
    bef_arr = nums[:k+1] + sorted(nums[k+1:], reverse=True)
    print(*bef_arr)



n = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().strip().split(" ")))
solve()
