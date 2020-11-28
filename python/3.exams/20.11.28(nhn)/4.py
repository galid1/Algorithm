def solution():
    card = 11111101

    list_card = list(map(int, (str(card))))

    # 짝
    if len(list_card) % 2 == 0:
        for i in range(0, len(list_card), 2):
            list_card[i] *= 2
    # 홀
    else:
        for i in range(1, len(list_card), 2):
            list_card[i] *= 2

    answer = 0
    for num in list_card:
        if len(str(num)) == 1:
            answer += num
        else:
            list_num = list(map(int, str(num)))
            answer += sum(list_num)

    if answer % 10 == 0:
        return "VALID"
    else:
        return "INVALID"


print(solution())