from collections import deque


def solution(record):
    q = deque()
    first_sell_amount = 0
    for r in record:
        types, price, cnt = r.split(" ")
        price, cnt = int(price), int(cnt)

        if types == "P":
            q.append((price, cnt))
        else:
            sell_cnt = cnt
            while sell_cnt > 0:
                price, purchase_cnt = q.popleft()
                cur_sell_cnt = min(sell_cnt, purchase_cnt)

                first_sell_amount += cur_sell_cnt * price
                sell_cnt -= cur_sell_cnt
                purchase_cnt -= cur_sell_cnt

                if purchase_cnt > 0:
                    q.appendleft((price, purchase_cnt))

    q = deque()
    last_sell_amount = 0
    for r in record:
        types, price, cnt = r.split(" ")
        price, cnt = int(price), int(cnt)

        if types == "P":
            q.append((price, cnt))
        else:
            sell_cnt = cnt
            while sell_cnt > 0:
                price, purchase_cnt = q.pop()
                cur_sell_cnt = min(sell_cnt, purchase_cnt)

                last_sell_amount += cur_sell_cnt * price
                sell_cnt -= cur_sell_cnt
                purchase_cnt -= cur_sell_cnt

                if purchase_cnt > 0:
                    q.append((price, purchase_cnt))

    return [first_sell_amount, last_sell_amount]


record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
record = ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]
print(solution(record))