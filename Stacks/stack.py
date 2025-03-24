class Stack:
    def __init__(self):
        self.stack = []

    #push in stack
    def push(self , element):
        self.stack.append(element)

    #pop in stack
    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    #check stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    #size of stack
    def size(self):
        return len(self.stack)

    #display the stack
    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print(self.stack[::-1])

