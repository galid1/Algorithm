from queue import Queue

def solution(numbers, target):
    answer = 0

    q = Queue()
    q.put(-numbers[0])
    q.put(numbers[0])

    for i in range(1, len(numbers)):
        for j in range(q.qsize()):
            cur_num = q.get()

            # 더하고 뺀것 넣기
            q.put(cur_num - numbers[i])
            q.put(cur_num + numbers[i])

    for num in list(q.queue):
        if num == target:
            answer += 1

    return answer

solution([1,1,1,1,1], 3)