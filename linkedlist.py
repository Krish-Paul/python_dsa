#Define a class Node to describe a node of a singly linked list.
#Define a class SLL to implement Singly Linked List with _init__() method to create and initialise start reference variable.
#Define a method is _emptyl) to check if the linked list is empty in SLL class.
#In class SLL, define a method insert_at_start) to insert an element at the starting ofthe list.
#In class SLL, define a method insert _at _last) to insert an element at the end of the list.
#In class SLL, define a method search) to find the node with specified element value
#In class SLL, define a method insert_after) to insert a new node after a given node of the list.
#In class SLL, define a method to print ali the elements of the list.
#In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
# In class SLL, define a method delete _first) to delete first element from the list.


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
