goods = [10, 15, 20, 23, 24, 25, 30, 40, 50, 51, 52]
# a = [46,62,9]
# a = [50,62,93]
# a = [5,31,15]
# a = [5,3,15]

def solution():
    global goods
    goods.sort()

    # 정답
    answer = 0

    # 50보다 큰 인덱스 찾기
    greater_fifty_idx = -1
    for i in range(len(goods)):
        if goods[i] >= 50:
            greater_fifty_idx = i
            break

    if greater_fifty_idx != -1:
        # 50보다 이미 큰 계산 처리
        answer += process_greater_than_fifty(goods, greater_fifty_idx)
        # 50보다 작은 계산 처리
        answer += process_less_than_fifty(goods[:greater_fifty_idx])
    else:
        answer += process_less_than_fifty(goods)

    return answer


def process_greater_than_fifty(a, greater_fifty_idx):
    sums = 0
    greater_count = 0
    for i in range(greater_fifty_idx, len(a)):
        sums += a[i]
        greater_count += 1

    sums -= 10 * greater_count
    return sums


def process_less_than_fifty(less_that_fifty_arr):
    sums = 0
    pair = 0

    temp_sums = 0
    while less_that_fifty_arr:
        temp_sums += less_that_fifty_arr[0]
        del less_that_fifty_arr[0]

        for i in range(len(less_that_fifty_arr)):
            if temp_sums + less_that_fifty_arr[i] >= 50:
                sums += temp_sums + less_that_fifty_arr[i]
                del less_that_fifty_arr[i]
                temp_sums = 0
                pair += 1
                break

    sums += temp_sums
    if temp_sums >= 50:
        sums -= 10
    sums = sums - 10 * pair

    return sums

print(solution())


