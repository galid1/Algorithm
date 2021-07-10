class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head):
    # linked list의 원소가 1개 이하
    if not head or not head.next:
        return head

    even_list_head = self.get_even_list(head)

    p = even_list_head
    while head and p:
        new_node = ListNode(head.val)
        new_node.next = p.next
        p.next = new_node
        p = new_node.next

        head = head.next.next

        if not p and head:
            new_node.next = ListNode(head.val)

    return even_list_head


def get_even_list(self, head):
    tmp_head = head.next
    new_head = new_tail = ListNode(tmp_head.val)

    while tmp_head and tmp_head.next:
        tmp_head = tmp_head.next.next

        if not tmp_head:
            break

        new_node = ListNode(tmp_head.val)
        new_tail.next = new_node
        new_tail = new_tail.next

    return new_head



seven = ListNode(3)
six = ListNode(6, seven)
five = ListNode(5, six)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2,three)
one = ListNode(1, two)
swapPairs(one)
