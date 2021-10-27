from collections import Counter
import sys


def minOperations(n):
    # Write your code here
    bin_n = bin(n)
    ans = sys.maxsize

    one_cnt = Counter(str(bin_n)[2:])['1']
    start = list(bin_n[2:])
    str_start = ''.join(start)
    visited = set()
    visited.add(str_start)

    stack = [[one_cnt, start, 0]]

    while stack:
        cnt, cur, depth = stack.pop()

        if depth >= ans:
            continue

        if cnt == 0:
            ans = min(ans, depth)
            continue

        if cur[-1] == '1':
            cur[-1] = '0'
            str_cur = ''.join(cur)
            if str_cur not in visited:
                visited.add(str_cur)
                stack.append([one_cnt - 1, cur.copy(), depth + 1])
            cur[-1] = '1'
        else:
            cur[-1] = '1'
            str_cur = ''.join(cur)
            if str_cur not in visited:
                visited.add(str_cur)
                stack.append([one_cnt + 1, cur.copy(), depth + 1])
            cur[-1] = '0'

        position = verify_first_condition(cur)
        if position == -1:
            continue

        if cur[position] == '1':
            cur[position] = '0'
            str_cur = ''.join(cur)
            if str_cur not in visited:
                visited.add(str_cur)
                stack.append([one_cnt - 1, cur.copy(), depth + 1])
            cur[position] = '1'
        else:
            cur[position] = '1'
            str_cur = ''.join(cur)
            if str_cur not in visited:
                visited.add(str_cur)
                stack.append([one_cnt + 1, cur.copy(), depth + 1])
            cur[position] = '0'


    print(ans[0])
    return ans[0]


def verify_first_condition(bin_n):
    flag = False
    for idx in range(len(bin_n) - 1, -1, -1):
        if flag:
            return idx

        if bin_n[idx] == '1':
            flag = True

    return -1


print(minOperations(10000000))
