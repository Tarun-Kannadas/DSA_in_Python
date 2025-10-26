class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class addval:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      print("Linked List: ")
      while printval is not None:
         print (printval.data, end=" ")
         printval = printval.next

   def AddAtBeginning(self,newdata):
      NewNode = Node(newdata)

      NewNode.next = self.head
      self.head = NewNode

   def AddAtEnd(self,newdata):
      NewNode = Node(newdata)

      NewNode.next = self.head
      self.head = NewNode

l1 = addval()
l1.head = Node("564")
e2 = Node("132")
e3 = Node("77")

l1.head.next = e2
e2.next = e3

l1.AddAtBeginning("56")
l1.AddAtEnd("63")
l1.listprint()