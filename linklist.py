class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next  = new_node
            self.tail = new_node
            self.length+=1
    def __str__(self):
        temp_node = self.head
        result = '"'
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    def insert(self,index,value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
                new_node.next = temp_node.next
                temp_node.next = new_node
        self.length += 1
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current =  current.next
    def search(self,target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index = index + 1
        return -1
    def get(self,index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.value
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length = self.length -1
            return popped_node

    def pop(self):
            popped_node = self.tail
            if self.length == 0:
                return None
            elif self.length == 1:
                self.head = None
                self.tail = None
                return popped_node
            else:
                temp = self.head
                while temp.next is not self.tail:
                    temp = temp.next
                    temp.next = None

            self.length = self.length - 1
            return popped_node

    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index >+ self.length or index <0:
            return None
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length = self.length - 1
        return popped_node












new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(40)
new_linked_list.prepend(50)
new_linked_list.traverse()
print(new_linked_list.search(50))
print(new_linked_list.get(3))
print(new_linked_list)
print(new_linked_list.pop())
print(new_linked_list)

print(new_linked_list.remove(1))
