class Node:
    def __init__(self, val: int = -1):
        self.val=val
        self.next=None


class MyHashSet:

    def __init__(self):
        self.head = Node()
        self.tail = Node(10000001)
        self.head.next = self.tail
        self.tail.next = None
        

    def add(self, key: int) -> None:
        temp = Node(key)
        i = self.head

        while i!=self.tail:
            if i.next.val>temp.val:
                temp.next = i.next
                i.next = temp
                return
            elif i.next.val==temp.val:
                return
            else:
                i=i.next

        

    def remove(self, key: int) -> None:
        i = self.head;
        while i!=self.tail:
            if i.next.val == key:
                t = i.next
                i.next = i.next.next
                t.next = None
            i=i.next
        

    def contains(self, key: int) -> bool:
        i = self.head;
        while i!=self.tail:
            if i.next.val == key:
               return True
            i=i.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)