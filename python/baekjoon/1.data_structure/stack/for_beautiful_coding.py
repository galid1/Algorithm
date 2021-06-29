# baekjoon 2879 코딩은 예쁘게

import sys
import collections

def for_beautiful_coding(origin, purpose):
    diff_group = collections.deque()
    # 결과 값
    result = 0

    while origin:
        # 음, 양 파악
        fir_diff = origin.pop() - purpose.pop()
        zero = 0

        # 빼내고 다음 수가 없는 경우
        if not origin:
            result += abs(fir_diff)
            continue

        # 차이가 0인 경우
        if fir_diff == 0:
            continue

        # 기본적으로 음인 경우 (그룹핑만 하는방법이 달라지고 나머지는 음, 양 똑같음)
        if origin:
            cur_diff = origin[-1] - purpose[-1]
            # 양인 경우 바꿈
            if fir_diff > 0:
                cur_diff, zero = zero, cur_diff

            # 부호 체크 끝난 후 fir_diff 를 넣음
            diff_group.append(abs(fir_diff))

            while origin and cur_diff < zero:
                diff_group.append(abs(origin.pop() - purpose.pop()))
                if origin:
                    cur_diff = origin[-1] - purpose[-1]
                    # 양인 경우 바꿈
                    if fir_diff > 0:
                        zero = 0
                        cur_diff, zero = zero, cur_diff

        # 그룹이 비지 않을때 까지
        while diff_group:
            # 맨앞이 0인 경우 제거
            if diff_group[0] == 0:
                diff_group.popleft()
                continue

            # 앞에서부터 가장작은 차이를 가진것을 찾아 0 앞까지 더함
            min_diff = diff_group[0]
            # 가장 작은 차이를 가진 인덱스와 그 값을 찾는다
            for i in range(len(diff_group)):
                if diff_group[i] == 0:
                    break

                if diff_group[i] < min_diff:
                    min_diff = diff_group[i]

            # 결과에 인덴트 횟수를 더함
            result += abs(min_diff)
            # 찾은 제일 작은 차이만큼 0아닌애 앞까지 더함
            for i in range(len(diff_group)):
                if diff_group[i] == 0:
                    break
                diff_group[i] = diff_group[i] - min_diff

    print(result)


N = int(sys.stdin.readline())
origin = list(map(int, sys.stdin.readline().rstrip().split(" ")))
purpose = list(map(int, sys.stdin.readline().rstrip().split(" ")))
origin.reverse()
purpose.reverse()
for_beautiful_coding(origin, purpose)
