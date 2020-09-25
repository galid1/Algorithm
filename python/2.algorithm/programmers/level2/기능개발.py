# 1. 전체배열을 순회하며 속도만큼 더한다
# 2. 맨 앞을 확인하여 배포 가능한지 본다
# 3. 배포가 가능하다면 순회하며, 하나씩 제거하며 배포수를 증가시킨다.
# 4. 배포가 끝나면 결과에 배포수를 넣는다

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        # 진행
        while progresses[0] < 100:
            for si in range(len(speeds)):
                progresses[si] += speeds[si]

        # 배포 확인
        count = 0
        for progress in progresses:
            if progress >= 100:
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)

            for j in range(count):
                progresses.popleft()
                speeds.popleft()

    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))