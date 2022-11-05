class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while temp and i <= index:
            temp = temp.next
            i += 1
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        i = 0
        while temp and i < index:
            temp = temp.next
            i += 1
        if not temp: return
        node = Node(val)
        node.next = temp.next
        temp.next = node

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        i = 0
        while temp and i < index:
            temp = temp.next
            i += 1
        if not temp or not temp.next: return
        temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)