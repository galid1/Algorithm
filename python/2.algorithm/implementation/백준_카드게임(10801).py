import sys

def solve():
    global a_cards, b_cards

    v_cnt = [0, 0]
    for i in range(len(a_cards)):
        if a_cards[i] > b_cards[i]:
            v_cnt[0] += 1
        elif a_cards[i] < b_cards[i]:
            v_cnt[1] += 1

    if v_cnt[0] > v_cnt[1]:
        print("A")
    elif v_cnt[0] < v_cnt[1]:
        print("B")
    else:
        print("D")


a_cards = list(map(int, sys.stdin.readline().strip().split(' ')))
b_cards = list(map(int, sys.stdin.readline().strip().split(' ')))
solve()