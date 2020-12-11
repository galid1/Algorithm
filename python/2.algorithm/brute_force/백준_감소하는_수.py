import sys


def dfs(cur_num):
    global n, answer, idx, printed, answers

    for i in range(10):
        new_num = cur_num + str(i)

        # 정답
        if n == idx:
            if not printed:
                print(answer)
            printed = True
            return

        if is_decreasing(new_num):
            idx += 1
            answer = new_num
            answers.append(new_num)
        else:
            break

    for j in range(0, 10):
        init = ''
        if cur_num:
            init = cur_num[:-1]
            new_num = init + str(int(cur_num[-1]) + j)
        else:
            new_num = 

        if not is_decreasing(new_num):
            continue
        dfs(new_num)


def is_decreasing(num):
    bef = num[0]

    for i in range(1, len(num)):
        if int(bef) <= int(num[i]):
            return False

        bef = num[i]

    return True


printed = False
answers = []
answer, idx = 0, -1
n = int(sys.stdin.readline())
dfs('')
if not printed:
    print(-1)
print(answers)