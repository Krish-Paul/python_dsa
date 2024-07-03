#Define a class Node to describe a node of a doubly linked list.
#Define a class DLL to implement Doubly Linked List with _init_() method to create and initialise start reference variable.
#Define a method is_empty) to check if the linked list is empty in DLL class.
#In class DLL, define a method insert _at_start) to insert an element at the starting of the list.
#In class DLL, define a method insert _at_last) to insert an element at the end of the list.
#In class DLL, define a method search) to find the node with specified element value
#In class DLL, define a method insert _after) to insert a new node after a given node of the list.
#In class DLL, define a method to print all the elements of the list.
#In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.



class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
