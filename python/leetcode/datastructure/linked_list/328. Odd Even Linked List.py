class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head or not head.next:
        return head

    ol_h = ol_t = ListNode(head.val)
    head = head.next
    el_h = el_t = ListNode(head.val)
    head = head.next

    while head:
        ol_t.next = ListNode(head.val)
        ol_t = ol_t.next
        head = head.next

        if not head:
            break

        el_t.next = ListNode(head.val)
        el_t = el_t.next
        head = head.next

    ol_t.next = el_h
    return ol_h


def pl(head):
    print("====")
    while head:
        print(head.val, end=' ')
        head = head.next


seven = ListNode(7)
six = ListNode(6, seven)
five = ListNode(5, six)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

oddEvenList(one)
