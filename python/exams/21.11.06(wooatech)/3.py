def solution(ings, menu, sell):
    answer = 0

    menu_map = init(ings, menu)

    for line in sell:
        name, cnt = line.split(" ")
        cnt = int(cnt)

        answer += (menu_map[name] * cnt)

    return answer


def init(ings, menu):
    ings_map = {}
    for line in ings:
        res = line.split(" ")
        ings_map[res[0]] = int(res[1])

    menu_map = {}
    for line in menu:
        name, ings, price = line.split(" ")

        menu_map[name] = int(price)

        for ing in list(ings):
            menu_map[name] -= ings_map[ing]

    return menu_map



ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

ings = ["x 25", "y 20", "z 1000"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BBBB 3", "TTT 2"]
print(solution(ings, menu, sell))