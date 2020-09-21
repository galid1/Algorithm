def solution(numbers):
    answer = 0

    numbers = list(numbers)

    target_list = []
    # 자리수를 증가시키며 모든 조합을 이용해 수 만들기
    for digit in range(1, len(numbers)+1):
        visit = [0 for i in range(len(numbers))]
        make_num(target_list, digit, numbers, [], visit)

    #소수 세기
    for t in target_list:
        if is_prime(t):
            answer += 1

    return answer


def make_num(target_list, digit, numbers, cur_num, visit):
    if len(cur_num) == digit:
        target = int(''.join(cur_num))
        if target not in target_list:
            target_list.append(target)
        return

    for ni in range(len(numbers)):
        if visit[ni]:
            continue

        visit[ni] = 1
        cur_num.append(numbers[ni])
        make_num(target_list, digit, numbers, cur_num, visit)
        visit[ni] = 0
        cur_num.pop()


def is_prime(num):
    count = 0
    if num <= 1:
        return False

    for i in range(1, num+1):
        if num%i == 0:
            count += 1
        if count > 2:
            return False

    return True


print(solution('17'))
