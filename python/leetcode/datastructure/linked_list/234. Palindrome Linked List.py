# 배열로 풀기
# def isPalindrome(head):
#     length = len(head)
#     for i in range(length//2):
#         if head[i] != head[length-1-i]:
#             return False
#
#     return True

# deque로 풀기
# from collections import deque
#
# def isPalindrome(head):
#     head = deque(head)
#
#     while head:
#         L = head.popleft()
#         if not head:
#             return True
#
#         R = head.pop()
#         if L != R:
#             return False
#
#     return True

# Linked List Node로 풀기
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# from collections import deque
#
# def isPalindrome(head):
#     if not head.next:
#         return True
#
#     q = deque()
#     while head:
#         q.append(head.val)
#         head = head.next
#
#     while len(q) > 1:
#         if q.popleft() != q.pop():
#             return False
#
#     return True

# runner를 이용한 풀이
def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = fast = head
    reverse = []
    while fast:
        if not fast.next:
            slow = slow.next
            break
        reverse.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    while reverse:
        if slow.val != reverse.pop():
            return False
        slow = slow.next

    return True

seven = ListNode(3)
six = ListNode(1, seven)
five = ListNode(2, six)
four = ListNode(3, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

print(isPalindrome(one))