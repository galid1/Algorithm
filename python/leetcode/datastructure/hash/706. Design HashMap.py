class ListNode:
    def __init__(self, val, key, next=None):
        self.val = val
        self.key = key
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hash_table = [ListNode(key=None, val=None) for _ in range(self.size)]

    def _hash(self, value):
        return value%self.size

    def put(self, key: int, value: int) -> None:
        hash_code = self._hash(key)
        new_node = ListNode(val = value, key= key)

        head = bef = self.hash_table[hash_code]
        while head and head.key != key:
            bef = head
            head = head.next

        # 해당 키가 버킷내에 존재하지 않음
        if not head:
            bef.next = new_node
            return

        new_node.next = head.next
        bef.next = new_node

    def get(self, key: int) -> int:
        hash_code = self._hash(key)
        head = self.hash_table[hash_code]

        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hash_code = self._hash(key)
        head = bef = self.hash_table[hash_code]

        while head and head.key != key:
            bef = head
            head = head.next

        if not head:
            return

        bef.next = head.next


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(3, 2)
print(myHashMap.get(2))
# print(myHashMap.get(1))
# print(myHashMap.get(3))
# print(myHashMap.put(2, 1))
# print(myHashMap.get(2))
# print(myHashMap.remove(2))
