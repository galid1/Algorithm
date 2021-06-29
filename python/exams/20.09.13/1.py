def solution(boxes):
    count = {}

    for box in boxes:
        for num in box:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

    odd = 0
    for i in count.values():
        if i%2 != 0:
            odd += 1

    answer = odd//2

    return answer
