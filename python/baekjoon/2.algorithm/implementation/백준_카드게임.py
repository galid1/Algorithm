import sys


def solve():
    global cards

    max_num = int(cards[0][1])
    color_all_same = True
    num_straight = True
    color = cards[0][0]
    num = cards[0][1]
    for i in range(1, len(cards)):
        max_num = max(max_num, int(cards[i][1]))

        if color != cards[i][0]:
            color_all_same = False

        if int(num) + 1 != int(cards[i][1]):
            num_straight = False
        else:
            num = int(cards[i][1])

    # 1
    if color_all_same and num_straight:
        return print(max_num + 900)
    # 4
    if color_all_same:
        return print(max_num + 600)
    # 5
    if num_straight:
        return print(max_num + 500)

    num_cnt = {i:0 for i in range(1, 10)}
    for color, num in cards:
        num_cnt[int(num)] += 1

    four, three, two, a_two = False, False, False, False
    four_num, three_num, two_num, a_two_num = 0, 0, 0, 0
    for num, cnt in num_cnt.items():
        if cnt == 4:
            four = True
            four_num = int(num)
        elif cnt == 3:
            three = True
            three_num = int(num)
        elif cnt == 2:
            if two:
                a_two = True
                a_two_num = int(num)
                continue
            two = True
            two_num = int(num)
    # 2
    if four:
        return print(four_num + 800)
    # 3
    if three and two:
        return print((three_num*10) + two_num + 700)
    # 6
    if three:
        return print(three_num + 400)
    # 7
    if two and a_two:
        if two_num > a_two_num:
            return print((two_num*10) + a_two_num + 300)
        else:
            return print((a_two_num*10) + two_num + 300)
    # 8
    if two:
        return print(two_num + 200)

    # 9
    print(max_num + 100)



cards = []
for _ in range(5):
    cards.append(tuple(sys.stdin.readline().strip().split(" ")))
cards = sorted(cards, key=lambda card: card[0])
cards = sorted(cards, key=lambda card: card[1])
solve()

# 1
# B 1
# B 2
# B 3
# B 4
# B 5

# 2
# B 1
# Y 1
# R 1
# G 1
# B 5

# 3
# B 1
# Y 1
# R 1
# G 2
# B 2

# 4
# B 1
# B 3
# B 2
# B 4
# B 6

# 5
# B 1
# Y 2
# R 3
# G 4
# B 5

# 6
# B 1
# G 1
# R 1
# Y 2
# Y 4

# 7
# B 1
# Y 1
# G 2
# B 2
# R 3
# 321

# 8
# B 1
# Y 1
# G 2
# B 4
# R 3
# 201

# 9
# B 1
# Y 6
# G 2
# B 4
# R 3