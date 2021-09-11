import math

def solution(n):
    answer = []

    prime_board = make_prime_board(n)

    divide([i for i in range(1, n+1)], prime_board, answer)

    return answer


def divide(arr, primes, answer):
    if len(arr) == 1:
        answer.append(arr[0])
        return

    # find prime
    for p in primes:
        if len(arr)%p == 0:
            break

    arrs = [[] for _ in range(p)]
    for idx, num in enumerate(arr):
        arrs[idx%p].append(num)

    for ar in arrs:
        divide(ar, primes, answer)


def make_prime_board(n):
    array = [True for _ in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n+1) if array[i] ]


answer = []
print(solution(12))
# solution(18)


# 다음과 같은 어떤 배열을 섞는 과정을 정의합니다.
#
# 주어진 배열의 길이(len이라고 정의합니다.)를 나누었을 때 나머지가 0이 되는 가장 작은 소수 p를 찾습니다. len=1 이라면 과정을 종료합니다.
# 각 길이가 len/p인 p개의 작은 배열 arr[1], arr[2], ..., arr[p]를 만듭니다.
# 기존 배열의 원소를 작은 것부터 큰 것까지 arr[1], arr[2], ..., arr[p], arr[1], arr[2], ... 순서로 넣습니다. 즉, arr[1]에 첫 번째 원소, arr[2]에 두 번째 원소, ..., arr[p]에 p번째 원소, arr[1]에 p+1번째 원소, arr[2]에 p+2번째 원소, ..., arr[p]에 마지막 원소를 넣습니다.
# p개 배열에 대해 같은 과정을 반복하고 기존 배열을 arr[1], arr[2], ..., arr[p]를 순서대로 이어 붙인 결과로 대체합니다.
# 예를 들어, 다음 그림은 n=12 일 때 배열을 섞는 과정을 표현한 것입니다.
#
# ex12.png
#
# [1,2,3,4,5,6,7,8,9,10,11,12]를 섞을 때, p=2이므로, 두 개의 배열 arr[1], arr[2]를 만들고, 1부터 12까지 오름차순 순서대로 번갈아가면서 두 배열에 원소를 분배합니다. 그 결과는 [1,3,5,7,9,11], [2,4,6,8,10,12]이고, 두 배열을 각각 재귀적으로 섞은 뒤 다시 합칩니다.
# [2,6,10]을 섞을 때, p=3이므로, 세 개의 배열 arr[1], arr[2], arr[3]을 만들고, 2, 6, 10을 오름차순 순서대로 번갈아가면서 세 배열에 원소를 분배합니다. 그 결과는 [2], [6], [10]이고, 세 배열을 각각 재귀적으로 섞은 뒤 다시 합칩니다.
# 이런 식으로 모든 과정을 완료하면 최종 결과는 [1,5,9,3,7,11,2,6,10,4,8,12]가 됩니다.
# 정수 n이 매개변수로 주어졌을 때, 1, 2, 3, ..., n 으로 배열을 만들고 문제에 주어진 과정을 통해 그 배열을 섞었을 때 결과로 나오는 배열을 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 2 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 12	[1,5,9,3,7,11,2,6,10,4,8,12]
# 18	[1,7,13,3,9,15,5,11,17,2,8,14,4,10,16,6,12,18]
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
# 입출력 예 #2
#
# 다음 그림은 n=18 일 때 배열을 섞는 과정을 표현한 것입니다.
# ex18.png