import sys


def solve():
    global num

    answer = 0
    arr = []

    for i in range(num // 2 + 1, num + 1):
        tmp_answer, tmp_arr = execute(num, i)

        if tmp_answer > answer:
            answer, arr = tmp_answer, tmp_arr


    print(answer)
    print(*arr)


def execute(start, second):
    result_cnt = 2
    result = [start, second]

    first = start
    second = second

    while True:
        next = first - second

        if next < 0:
            break

        first = second
        second = next

        # 정답 추가
        result.append(next)
        result_cnt += 1

    return result_cnt, result


num = int(sys.stdin.readline().strip())
solve()
