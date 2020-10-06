# 1. 제일 무거운 사람을 제일 가벼운 사람과 짝을 먼저 지은다
# 2. 제일 가벼운 사람과도 같이 구명보트를 타지 못한다면 그사람은 무조건 혼자 타야한다

def solution(people, limit):
    answer = 0

    people.sort()

    min_idx = 0
    max_idx = len(people) - 1

    while max_idx >= min_idx:
        if min_idx == max_idx:
            if people[max_idx] <= limit:
                answer += 1
                break

        if people[min_idx] + people[max_idx] <= limit:
            min_idx += 1
            max_idx -= 1
            answer += 1
        else:
            max_idx -= 1
            answer += 1

    return answer

solution([70, 50, 80, 50], 100)
solution([7, 5, 8, 5], 14)
solution([1, 1, 1, 1], 1)