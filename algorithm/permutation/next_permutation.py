import sys
# 다음순열 구하기
# 첫 순열은 오름차순일 수 밖에 없음
# 마지막 순열은 내림차순 일 수 밖에 없음 => 주어진 배열에서 a[i] < a[i+1] 이 존재하지 않으면 내림차순임

def next_permutation(numerate):
    is_changed = False

    for i in range(len(numerate)-1, 0, -1):
        if numerate[i] > numerate[i-1]:
            min = i
            for j in range(i, len(numerate)):
                if numerate[min] > numerate[j] and numerate[i-1] < numerate[j]:
                    min = j

            temp = numerate[i-1]
            numerate[i-1] = numerate[min]
            numerate[min] = temp
            is_changed = True

            # 이후 자리 정렬
            part_sort(numerate, i)
            break

    if is_changed is not True:
        return -1

    return numerate

def part_sort(list, start):
    for i in range(start, len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        if list[i] > list[min]:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

# 사용자 입력
n = int(sys.stdin.readline())
numerate = list(map(int, sys.stdin.readline().strip().split(" ")))
print(next_permutation(numerate))