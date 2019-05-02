# 프로그래머스 스킬체크 lv2 .2
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때,
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 입출력
# 93 30 55
# 1 30 5
# return 2 1

import sys

def solution(progresses, speeds):
    progresses.reverse()
    speeds.reverse()

    answer = []

    while progresses:
        for i in range(len(speeds)):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]

        count = 0

        if progresses[-1] >= 100:
            for j in range(len(progresses)):
                if progresses[-1] >= 100:
                    progresses.pop()
                    speeds.pop()
                    count += 1
                    continue
                break
            answer.append(count)

    return(answer)

progresses = list(map(int, sys.stdin.readline().rstrip().split(" ")))
speeds = list(map(int, sys.stdin.readline().rstrip().split(" ")))
solution(progresses, speeds)
