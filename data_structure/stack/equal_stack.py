import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    # 새로운 배열을 만들어 그것에는 만들 수 있는 길이를 담음
    old_lists = [h1, h2, h3]
    new_lists = [[h1.pop()], [h2.pop()], [h3.pop()]]

    for i in range(3):
        while len(old_lists[i]) > 0:
            new_lists[i].append(new_lists[i][-1] + old_lists[i].pop())

    min = -1
    min_stack = None
    # 세 스택중 하나라도 비게 되면 0을 리턴
    while new_lists[0] and new_lists[1] and new_lists[2]:
        # 제일 짧은 스택 찾기
        for list in new_lists:
            if min > list[-1] or min is -1:
                min = list[-1]
                min_stack = list

        cans = []
        for list in new_lists:
            if list is min_stack:
                continue
            while list and list[-1] > min:
                list.pop()
            if min in list:
                cans.append(True)

        if len(cans) is 2:
            return min
        elif min_stack:
            min_stack.pop()

    return 0

if __name__ == '__main__':

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)