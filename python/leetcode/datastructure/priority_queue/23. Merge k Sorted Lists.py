import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    sorted_list = []

    for li in lists:
        head = li
        while head:
            heapq.heappush(sorted_list, head.val)
            head = head.next

    head = tail = None
    while sorted_list:
        val = heapq.heappop(sorted_list)

        new_node = ListNode(val)

        if not head:
            head = tail = new_node
            continue

        tail.next = new_node
        tail = tail.next

    return head


lists = [[1,4,5],[1,3,4],[2,6]]
new_lists = []
for li in lists:
    new_lists.append(list(map(lambda e: ListNode(e), li)))

mergeKLists(new_lists)