from collections import deque


def solution(ball, order):
    ball = deque(ball)
    answer = []
    holder = {}

    for o in order:
        pop_in_holder(holder, ball, answer)

        # 맨 앞 또는 맨 뒤에 존재하는지 파악
        pop_ball = None
        if o == ball[0]:
            pop_ball = ball.popleft()
        elif o == ball[-1]:
            pop_ball = ball.pop()

        # 우선순위 대기열에 삽입
        if not pop_ball:
            holder[o] = o
        else:
            answer.append(pop_ball)

    return answer


def pop_in_holder(holder, ball, answer):
    for h in holder:
        if h == ball[0]:
            answer.append(h)
            ball.popleft()
            pop_in_holder(holder, ball, answer)
            return
        elif h == ball[-1]:
            answer.append(h)
            ball.pop()
            pop_in_holder(holder, ball, answer)
            return


# print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
# print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))