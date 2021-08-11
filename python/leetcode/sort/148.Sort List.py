# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        l_head, r_head = head, self.get_half_head(head)

        l_head = self.sortList(l_head)
        r_head = self.sortList(r_head)

        return self.merge(l_head, r_head)

    def get_half_head(self, head):
        half, slow, fast = None, head, head
        while fast and fast.next:
            half = slow
            slow = slow.next
            fast = fast.next.next
        half.next = None

        return slow

    def merge(self, l_head, r_head):
        head = tail = ListNode()

        while l_head and r_head:
            if l_head.val <= r_head.val:
                tail.next = l_head
                l_head = l_head.next
            else:
                tail.next = r_head
                r_head = r_head.next
            tail = tail.next

        while l_head:
            tail.next = l_head
            l_head = l_head.next
            tail = tail.next

        while r_head:
            tail.next = r_head
            r_head = r_head.next
            tail = tail.next

        return head.next


head = [4,2,1,3]
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

tmp = head
while tmp:
    print(tmp.val)
    tmp = tmp.next

s = Solution()
head = s.sortList(head)

while head:
    print(head.val)
    head = head.next