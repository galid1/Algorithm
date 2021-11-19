import sys


def dfs(cur):
    global visited, ans

    if ans:
        return

    if len(cur) == 7:
        update(cur)
        return

    for i in range(10):
        if visited[i]:
            continue

        visited[i] = True
        cur.append(i)
        dfs(cur)
        cur.pop()
        visited[i] = False


def update(nums):
    global ans, target

    if nums[2] == 0 or nums[6] == 0:
        return

    hello = nums[2] * 10000 + nums[1] * 1000 + nums[3] * 100 + nums[3] * 10 + nums[4]
    world = nums[6] * 10000 + nums[4] * 1000 + nums[5] * 100 + nums[3] * 10 + nums[0]

    if hello + world == target:
        ans = hello, world


visited = [False for _ in range(10)]
target = int(sys.stdin.readline().strip())
ans = ()
dfs([])

if not ans:
    print("No Answer")
else:
    print("  %d" %ans[0])
    print("+ %d" %ans[1])
    print("-------")
    if target >= 100000:
        print(" %d" %target)
    else:
        print("  %d" %target)