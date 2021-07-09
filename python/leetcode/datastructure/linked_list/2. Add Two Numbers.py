class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    l1_len, l2_len = get_len(l1), get_len(l2)

    # 길이를 비교하여 변경함 => 무조건 l1이 더 짧음
    if l1_len > l2_len:
        l1, l2 = l2, l1

    head = tail = None
    one = ten = 0
    # l1 다 소모할 때까지
    while l1:
        # 합 구하기
        sums = list(str(l1.val + l2.val + ten))
        # l1, l2 옮기기
        l1, l2 = l1.next, l2.next

        # 십의자리, 일의자리 만들기
        if len(sums) == 2:
            ten, one = map(int, sums)
        else:
            ten, one = 0, int(sums[0])

        new_node = ListNode(one)
        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    one = 0
    # l2 다 소모할 때까지
    while l2:
        sums = list(str(l2.val + ten))
        l2 = l2.next

        if len(sums) == 2:
            ten, one = map(int, sums)
        else:
            ten, one = 0, int(sums[0])

        new_node = ListNode(one)
        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    # 마지막 올림이 0보다 크면 !
    if ten > 0:
        tail.next = ListNode(ten)

    return head

def get_len(h):
    length = 0
    while h:
        length += 1
        h = h.next

    return length


def pl(h):
    print('====')
    while h:
        print(h.val, end=' ')
        h = h.next


four = ListNode(9, )
three = ListNode(4, four)
two = ListNode(6, three)
one = ListNode(5, two)

# four_2 = ListNode(4, )
three_2 = ListNode(9, )
two_2 = ListNode(4, three_2)
one_2 = ListNode(2, two_2)
pl(addTwoNumbers(one, one_2))


