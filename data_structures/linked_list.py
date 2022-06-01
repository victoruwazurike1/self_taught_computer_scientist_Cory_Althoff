from collections import deque


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # def __str__(self):
    #     node = self.head
    #     while node is not None:
    #         print(node.data)
    #         node = node.next

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = target.next
            previous = current
            current = current.next

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except slow is not fast:
                return False

    def print_list(self):
        current = self.head
        while current.next:
            current = current.next
            print(current.data)


a_list = LinkedList()
a_list.append('Monday')
a_list.append('Tuesday')
a_list.append('Wednesday')
a_list.append('Thursday')
a_list.append('Friday')
a_list.append('Saturday')
print(a_list.print_list())


# d = deque()
# d.append('Harry')
# d.append('Potter')


# print(a_list)
# print(d)
# for item in d:
#  print(item)
