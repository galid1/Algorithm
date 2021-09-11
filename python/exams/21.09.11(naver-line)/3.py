from collections import deque, defaultdict

def solution(jobs):
    answer = []
    jobs = deque(jobs)

    time = 0
    job_queue = defaultdict(list)
    bef_class = 0
    while jobs or job_queue:
        added = classify(job_queue, time, jobs)

        # jobqueue가 비고, 아무것도 안담기면 다음 요청 초까지 증가시킴
        if not job_queue and not added:
            time += 1
            continue

        # 다음 처리할 분류 가져오기
        next_class = get_next_class(job_queue, bef_class)
        bef_class = next_class

        # 처리 분류 정답에 추가
        if not answer:
            answer.append(next_class)
        elif answer[-1] != bef_class:
            answer.append(next_class)

        # job queue에서 제거
        next_jobs = job_queue.pop(next_class)

        # 작업 진행
        spend_time = do_process(next_jobs)
        time += spend_time

    return answer


def classify(job_queue, time, jobs):
    added = False

    while jobs and jobs[0][0] <= time:
        added = True
        job_queue[jobs[0][2]].append(jobs.popleft())

    return added


def get_next_class(job_queue, bef_class):
    if bef_class != 0:
        if len(job_queue[bef_class]) >= 1:
            return bef_class
        else:
            job_queue.pop(bef_class)


    next_job_class = 1000
    max_priority_sums = 0
    for class_num, jobs in job_queue.items():
        cur_sum = 0
        for job in jobs:
            cur_sum += job[3]

        if cur_sum >= max_priority_sums:
            if next_job_class > class_num:
                next_job_class = class_num
                max_priority_sums = cur_sum

    return next_job_class


def do_process(jobs):
    spend_time = 0

    for job in jobs:
        need_time = job[1]
        spend_time += need_time

    return spend_time


jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]
print(solution(jobs))

# from collections import defaultdict
#
# a = {'a': 1, 'b': 2}
# print(a)
# a.pop('a')
# print(a)

# 당신은 밀려드는 많은 작업을 효율적으로 처리하기 위해 다음과 같은 규칙에 따라 일을 하려고 합니다. 모든 작업은 각각의 중요도를 갖고 있으며, 처리하는 방식에 따라 여러 분류로 나눠집니다. 같은 처리 방식에 익숙해지면 편하게 일을 할 수 있기 때문에, 어떤 분류의 작업을 처리하기로 했다면 해당 분류의 작업들을 모두 끝마칠 때까지 작업을 처리합니다. 처리하는 도중이거나 처리가 끝남과 동시에 같은 분류의 작업이 새로 요청되었다면, 새로운 작업도 이어서 처리합니다. 한 분류에 속하는 모든 작업을 끝냈다면, 계속해서 다른 분류 중 작업의 중요도 합이 가장 높은 분류를 선택하여 처리합니다. 만약 중요도 합이 가장 높은 분류가 여러 개라면, 분류 번호가 가장 낮은 분류를 선택하여 처리합니다.
#
# 위와 같은 규칙에 따라 분류를 옮겨가면서 모든 일을 처리했을 때, 처리한 분류 번호의 순서를 알아보고자 합니다.
#
# 아래 표는 요청 시각을 기준으로 정렬한 작업 목록입니다. 이 문제에서 요청 시각이 같은 작업은 주어지지 않습니다.
#
# 번호	요청 시각(초)	걸리는 시간(초)	분류 번호	중요도
# 1번	1	5	2	3
# 2번	2	2	3	2
# 3번	3	1	3	3
# 4번	5	2	1	5
# 5번	7	1	1	1
# 6번	9	1	1	1
# 7번	10	2	2	9
# 1초: 요청 시각이 가장 빠른 1번 작업(분류: 2)을 선택합니다. 처리에 걸리는 시간은 5초입니다.
# 1초~6초: 1번 작업을 처리합니다. 그동안 2번, 3번, 4번 작업이 새로 요청되어 대기합니다.
# 6초: 분류 3에 속한 2번, 3번 작업의 중요도 합은 5입니다. 분류 1에 속한 4번 작업의 중요도는 5입니다. 중요도가 같다면 분류 번호가 낮은 분류를 선택합니다. 따라서 분류 1의 작업을 선택합니다.
# 6초~9초: 4번 작업을 8초까지 처리합니다. 그동안 같은 분류인 5번 작업이 요청되었습니다. 따라서 5번 작업을 이어서 9초까지 처리합니다.
# 9초~10초: 분류 1의 작업을 끝냄과 동시에 같은 분류인 6번 작업이 요청됩니다. 방금 처리가 끝난 분류와 새로 요청된 작업의 분류가 같은 경우, 이어서 해당 분류의 작업을 처리합니다. 따라서, 6번 작업을 이어서 처리합니다.
# 10초: 6번 작업을 처리함과 동시에 분류 2의 7번 작업이 요청됩니다. 어떤 분류의 작업을 모두 마침과 동시에 다른 분류의 작업 요청이 들어오면, 해당 요청까지 고려하여 다음 분류를 선택합니다. 따라서, 중요도 합이 더 높은 분류 2의 7번 작업을 처리합니다.
# 10초~12초: 7번 작업을 처리합니다.
# 12초~15초: 분류 3에 속한 2번과 3번 작업을 처리합니다.
# 따라서 위 예시에서는 분류를 2 → 1 → 2 → 3 순서대로 옮기며 작업을 처리했습니다.
#
# 작업의 요청 시각, 처리하는데 걸리는 시간, 분류, 중요도를 담은 2차원 정수 배열 jobs가 매개변수로 주어집니다. 위 규칙대로 작업을 처리했을 때, 처리한 분류 번호를 시간 순서대로 담아 return 하도록 solution 함수를 완성해주세요. 단, 어떤 분류의 작업을 이어서 처리하지 않았더라도 같은 분류 번호가 연속해서 나오지 않도록 주의해주세요. 예를 들어, 처리한 작업의 분류 순서가 1 → 1 → 2 → 1 이라면, 배열 [1, 2, 1]을 return 합니다.
#
# 제한사항
# 1 ≤ jobs의 길이 ≤ 10,000
# jobs의 원소는 [a, b, c, d] 형태입니다.
# a는 작업이 요청된 시각을 의미합니다. 모든 작업의 요청 시각은 서로 다릅니다.
# jobs는 요청 시각을 기준으로 오름차순 정렬되어 있습니다.
# 0 ≤ a ≤ 1,000,000
# b는 작업을 처리하는데 걸리는 시간을 의미합니다.
# 1 ≤ b ≤ 10,000
# c는 작업의 분류 번호를 의미합니다.
# 1 ≤ c ≤ 100
# d는 작업의 중요도를 의미합니다.
# 1 ≤ d ≤ 100
# 입출력 예
# jobs	result
# [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]	[2, 1, 2, 3]
# [[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]	[1, 2]
# [[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]	[3, 4]
# [[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]	[1, 3, 4]
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
#
# 입출력 예 #2
#
# 주어진 입력을 아래 표와 같이 정리할 수 있습니다.
#
# 번호	요청 시각(초)	걸리는 시간(초)	분류 번호	중요도
# 1번	1	2	1	5
# 2번	2	1	2	100
# 3번	3	2	1	5
# 4번	5	2	1	5
# 1초~3초: 가장 먼저 요청된 1번 작업(분류: 1)을 처리합니다. 그동안 2번 작업의 요청이 들어옵니다.
# 3초~5초: 3번 작업(분류: 1)이 1번 작업(분류: 1)이 끝남과 동시에 들어옵니다. 분류 번호가 같으므로 3번 작업을 처리합니다.
# 5초~7초: 4번 작업(분류: 1)이 3번 작업(분류: 1)이 끝남과 동시에 들어옵니다. 분류 번호가 같으므로 4번 작업을 처리합니다.
# 7초~8초: 남은 2번 작업(분류: 2)을 처리합니다.
# 순서대로 처리한 분류 번호는 1 → 2입니다. 따라서 배열 [1, 2]를 return 합니다.
#
# 입출력 예 #3
#
# 0초~2초: 1번 작업(분류: 3)을 처리합니다.
# 5초~8초: 2번 작업(분류: 3)을 처리합니다.
# 10초~12초: 3번 작업(분류: 4)을 처리합니다.
# 따라서 배열 [3, 4]를 return 합니다.
#
# 입출력 예 #4
#
# 0초~5초: 1번 작업(분류: 1)을 처리합니다. 2초에 2번 작업(분류: 3), 3초에 3번 작업(분류: 4)이 요청됩니다. 중요도 합은 각각 3, 5입니다.
# 5초: 1번 작업이 끝남과 동시에, 4번 작업(분류: 3)이 새로 요청됩니다. 해당 요청의 중요도까지 고려하면 3번 분류와 4번 분류의 중요도 합이 5로 같습니다. 따라서 번호가 낮은 3번 분류를 선택합니다.
# 5초~11초: 2번, 4번 작업(분류: 3)을 처리합니다.
# 11초~15초: 3번 작업(분류: 4)을 처리합니다.
# 따라서 배열 [1, 3, 4]를 return 합니다.