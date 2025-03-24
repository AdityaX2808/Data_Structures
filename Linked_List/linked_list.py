class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #insert node at the first of the linked list
    def insert_at_first(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert at the end of the linked  list
    def insert_at_end(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    #insert after the  given value
    def insert_after(self , data , value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    #insert before the given values
    def insert_before(self , data , value):
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next



    #delete from the first of the linked list
    def delete_at_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    #delete from the end of the linked list
    def delete_at_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    #delete the given value
    def delete_at_value(self , value):
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    #update at first
    def update_at_first(self , value):
        if self.head:
            self.head.data = value

    #update at last
    def update_at_last(self , value):
        current_node = self.head
        last = current_node
        while last.next:
            last = last.next
        last.data = value

    #update at given value
    def update_at_value(self , data , value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                current_node.data = data
                return
            current_node = current_node.next

    #display the linked list
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data , end = "->")
            current_node = current_node.next
        print("None")



















