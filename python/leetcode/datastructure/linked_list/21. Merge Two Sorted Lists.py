class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    head, tail = None, None

    while l1 and l2:
        new_node = None
        if l1.val <= l2.val:
            new_node = ListNode(l1.val)
            l1 = l1.next
        else:
            new_node = ListNode(l2.val)
            l2 = l2.next

        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    while l1:
        new_node = ListNode(l1.val)
        l1 = l1.next

        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    while l2:
        new_node = ListNode(l2.val)
        l2 = l2.next

        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    return head
