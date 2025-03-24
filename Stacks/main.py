from stack import Stack

def main():

    mystack = Stack()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.push(40)
    mystack.display()

    print(mystack.pop())
    mystack.display()

    print(mystack.isEmpty())

    print(mystack.size())

if __name__ == "__main__":
    main()

