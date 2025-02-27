#Define a class Node to describe a node of a singly linked list.
#Define a class SLL to implement Singly Linked List with _init__() method to create and initialise start reference variable.
#Define a method is _emptyl) to check if the linked list is empty in SLL class.
#In class SLL, define a method insert_at_start) to insert an element at the starting ofthe list.
#In class SLL, define a method insert _at _last) to insert an element at the end of the list.
#In class SLL, define a method search) to find the node with specified element value
#In class SLL, define a method insert_after) to insert a new node after a given node of the list.
#In class SLL, define a method to print ali the elements of the list.
#In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
# In class SLL, define a method delete _first) to delete first element from the list
# In class SLL, define a method delete_last to delete last element from the list.
# In class SLL, define a method delete _item) to delete specified element from the list.


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def printlist(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
class SLLiterate:
    def __init__(self,start):
        self.current=start
#driver code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.printlist()
mylist.delete_item(30)
print()
