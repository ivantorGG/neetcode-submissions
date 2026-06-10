class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        self.tail = self.tail if self.head else new_head
        self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = self.tail = ListNode(val, None)
        else:
            self.tail.next = ListNode(val, None)
            self.tail = self.tail.next

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            new = ListNode(val, self.head)
            self.tail = self.tail if self.head else new
            self.head = new
        else:
            curr = self.head
            for _ in range(index):
                curr, prev = curr.next, curr

            new = ListNode(val, curr)
            if index == self.length:
                self.tail = new
            prev.next = new

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next

            if index == self.length - 1:
                self.tail = curr
            curr.next = curr.next.next

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)