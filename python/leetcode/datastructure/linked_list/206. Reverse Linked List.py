class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head:
        return []

    r_head = ListNode(head.val)
    head = head.next

    while head:
        new_node = ListNode(head.val)
        head = head.next

        new_node.next = r_head
        r_head = new_node

    return r_head


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
reverseList(one)