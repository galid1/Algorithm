from queue import Queue

def solution(n):
    answer = []
    count = 0

    q = Queue()
    q.put(n)

    while True:
        # 세그먼트
        for i in range(q.qsize()):
            cur = q.get()

            # 정답확인
            if len(str(cur)) == 1:
                answer.append(count)
                answer.append(cur)
                return answer

            cut_and_sum(cur, q)

        count += 1

    return answer


def cut_and_sum(num, queue):
    num_str = str(num)

    for i in range(1, len(num_str)):
        head = num_str[:i]
        tail = num_str[i:]

        if len(tail) > 1 and tail[0] == '0':
            continue

        sum = int(head) + int(tail)
        queue.put(sum)


# print(solution(10007))
# print(solution(73425)) // [4, 3]
# print(solution(9))