class Node:
   def __init__(self,data=None):
      self.data = data
      self.next = None

class addVal:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      print("\nLinked List is: ")
      while printval is not None:
         print(printval.data, end=" ")
         printval = printval.next

   def AddAtBeginning(self, newdata):
      NewNode = Node(newdata)
      NewNode.next = self.head
      self.head = NewNode

   def AddAtEnd(self, newdata):
      NewNode = Node(newdata)
      if (self.head == None):
         self.head = NewNode
         return
      last = self.head
      while last.next:
         last = last.next
      last.next = NewNode
      

l1 = addVal()
l1.head = Node("53")
e2 = Node("65")
e3 = Node("75")
l1.head.next = e2
e2.next = e3

l1.listprint()
l1.AddAtBeginning("69")
l1.AddAtEnd("96")
l1.listprint()