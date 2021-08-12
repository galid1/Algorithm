# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        def insert_to_sorted_list(comparator):
            cur, bef = sorted_head.next, sorted_head
            new_node = ListNode(comparator.val)

            while cur:
                if cur.val >= new_node.val:
                    bef.next = new_node
                    new_node.next = cur
                    return

                bef = cur
                cur = cur.next

            bef.next = new_node

        # 빈 head 예외 처리
        if not head:
            return head

        # dummy head, 정렬된 리스트
        sorted_head = ListNode()
        sorted_head.next = ListNode(head.val)

        # 삽입 정렬
        comparator = head.next
        while comparator:
            insert_to_sorted_list(comparator)
            comparator = comparator.next

        return sorted_head.next

s = Solution()

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

sorted_head = s.insertionSortList(head)

while sorted_head:
    print(sorted_head.val)
    sorted_head = sorted_head.next
