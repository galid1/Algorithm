class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    # list 1개 이하
    if not head or not head.next:
        return head

    # 앞머리 구성
    idx = 1
    lh = lt = None
    while head and idx < left:
        new_node = ListNode(head.val)
        head, idx = head.next, idx + 1

        if not lh:
            lh = lt = new_node
            continue

        lt.next = new_node
        lt = lt.next

    # 중간 리버스 구성
    mh = mt = None
    while head and idx <= right:
        new_node = ListNode(head.val)
        head, idx = head.next, idx+1

        if not mh:
            mh = mt = new_node
            continue

        new_node.next = mh
        mh = new_node

    # 오른쪽 끝 구성
    rh = rt = None
    while head:
        new_node = ListNode(head.val)
        head = head.next

        if not rh:
            rh = rt = new_node
            continue

        rt.next = new_node
        rt = rt.next

    if not lh:
        lh = mh
    else:
        lt.next = mh
    mt.next = rh

    return lh


def pl(head):
    print("===")
    while head:
        print(head.val, end=' ')
        head = head.next



# seven = ListNode(7)
# six = ListNode(6, seven)
# five = ListNode(5, six)
# four = ListNode(4, five)
# three = ListNode(3, four)
two = ListNode(2,)
one = ListNode(1,two)

reverseBetween(one, 1, 2)
