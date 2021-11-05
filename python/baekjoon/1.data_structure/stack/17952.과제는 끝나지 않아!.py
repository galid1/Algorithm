import sys


def solve():
    global n, tasks

    task_stack = []
    c_task_num, c_grade, c_remain = -1, -1, -1

    ans = 0
    for task in tasks:
        task_num = task[0]

        if not exist_task(task_num):
            if is_tasking(c_task_num):
                continue
        else:
            if not is_tasking(c_task_num):
                task_stack.append([c_task_num, c_grade, c_remain])
            c_task_num, c_grade, c_remain = task

        c_remain -= 1

        if is_end(c_remain):
            ans += c_grade
            if not task_stack:
                c_task_num = -1
            else:
                c_task_num, c_grade, c_remain = task_stack.pop()

    print(ans)


def is_end(remain):
    return remain == 0


def exist_task(task_num):
    return task_num != 0


def is_tasking(task_num):
    return task_num == -1


n = int(sys.stdin.readline().strip())
tasks = []
for _ in range(n):
    tasks.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()
