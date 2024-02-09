class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        last_node = self.get_last_node()

        llstr = str()
        while last_node:
            llstr += str(last_node.data) + " --> "
            last_node = last_node.prev
        print(llstr)

    def get_length(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_ending(self, data):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()

        last_node.next = Node(data=data, next=None, prev=last_node)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise ValueError(f"invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if index - 1 == count:
                new_node = Node(data=data, next=itr.next, prev=itr)
                itr.next = new_node
                # if new_node.next:
                #     new_node.next.prev = new_node
                break
            count += 1
            itr = itr.next


dll = DoublyLinkedList()
dll.insert_at_begining(5)
dll.insert_at_begining(6)
dll.insert_at_begining(56)
dll.insert_at_begining(12)
dll.print_forward()
# print(dll.get_last_node())
dll.insert_at_ending(32)
# dll.print_backward()
print(dll.get_length())
dll.print_forward()
dll.insert_at(1, 66)
dll.print_forward()
dll.print_backward()
