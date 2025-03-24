class Queue:
    def __init__(self):
        self.queue = []

    #enqueue in queue
    def enqueue(self , element):
        return self.queue.append(element)

    #dequeue in queue
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.pop(0)

    #is empty queue
    def isEmpty(self):
        return len(self.queue) == 0

    #size of the queue
    def size(self):
        return len(self.queue)

    #display the queue
    def display(self):
        if self.isEmpty():
            print("Queue is empty...")
        else:
            print(self.queue)
