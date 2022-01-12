import sys


def solve():
    global n, arr, nums

    # nums 를 순회하며 제외할 번호를 선택
    # arr을 순회,
    # 현재 번호를 선택 같은 번호면 길이 증가 max 길이 교체, 제외할 번호인 경우 continue, 제외할 번호가 아닌 경우 현재 번호 교체, 길이 1로

    max_len = 1
    for except_num in nums:
        cur_len = 1
        cur_num = arr[0]
        for num in arr[1:]:
            if num == cur_num:
                cur_len += 1
                max_len = max(max_len, cur_len)

            else:
                if num == except_num:
                    continue
                else:
                    cur_num = num
                    cur_len = 1

    print(max_len)


n = int(sys.stdin.readline().strip())
arr = []
nums = set()

for _ in range(n):
    cur_num = int(sys.stdin.readline().strip())
    arr.append(cur_num)
    nums.add(cur_num)

solve()