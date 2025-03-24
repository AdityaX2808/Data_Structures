from linked_list import LinkedList

def main():
    ll = LinkedList()

    #insert implementation
    ll.insert_at_first(10)
    ll.display()
    ll.insert_at_end(30)
    ll.display()
    ll.insert_at_end(40)
    ll.display()
    ll.insert_after(20 , 30)
    ll.display()
    ll.insert_before(50 , 30)
    ll.display()
    ll.insert_after(60 , 30)
    ll.display()

    #delete implementation
    ll.delete_at_first()
    ll.display()
    ll.delete_at_last()
    ll.display()
    ll.delete_at_value(20)
    ll.display()

    #updating implementation
    ll.update_at_first(70)
    ll.display()
    ll.update_at_last(80)
    ll.display()
    ll.update_at_value(90 , 30)
    ll.display()


if __name__  == "__main__":
    main()
