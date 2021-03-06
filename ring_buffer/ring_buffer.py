from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        else:
            if self.current.next:
                self.current.value = item
                self.current = self.current.next
            else:
                self.current.value = item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.current_index = 0
        self.capacity = capacity

    def append(self, item):
        self.storage[self.current_index] = item
        
        if self.current_index == self.capacity-1:
            self.current_index = 0
        else:
            self.current_index += 1


    def get(self):
        return [item for item in self.storage if item]
