from queue import Queue

def main():
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)
    myQueue.enqueue(50)

    myQueue.display()

    myQueue.dequeue()
    myQueue.display()

    print(myQueue.isEmpty())

    print(myQueue.size())

if __name__ == "__main__":
    main()