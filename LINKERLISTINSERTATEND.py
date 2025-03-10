
#INsertion of node in front (Linked list)
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
#insert at the front of the link list
    def insertatbegginning(self,new_data):
        #Create of the new node
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return 
    #insertion at the end
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    #print the linkedlist
    def printlist(self):
        temp=self.head
        while temp:
            print(str(temp.data) +" ",end=" ")
            temp=temp.next

#Driver code
llist=Linkedlist()
llist.insertatbegginning(12)
llist.insertatbegginning(1)
llist.insertatbegginning(7)
llist.insertatbegginning(9)
llist.insertatbegginning(10)
llist.printlist()