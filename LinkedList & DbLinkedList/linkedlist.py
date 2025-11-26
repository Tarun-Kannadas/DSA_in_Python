class Node:
   def __init__(self,data=None):
      self.data = data
      self.next = None

class addVal:
   def listing(self):
      printval = self.head
      while printval is not None:
         print(printval.data, end = " ")
         printval = printval.next

   def AddAtBeginning(self, newdata):
      NewNode = Node(newdata)
      NewNode.next = self.head
      self.head = NewNode

   def AddAtEnd(self, newdata):
      NewNode = Node(newdata)
      if (self.head == None):
         self.head = NewNode
      last = self.head
      while(last.next):
         last = last.next
      last.next = NewNode

   def AddAtMiddle(self, newdata):
      NewNode = Node(newdata)

      length = 0
      temp = self.head
      while(temp):
         temp = temp.next
         length += 1

      mid = length // 2

      temp = self.head

      for _ in range(mid-1):
         temp = temp.next

      NewNode.next = temp.next
      temp.next = NewNode

l1 = addVal()
l1.head = Node(56)
e2 = Node(75)
e3 = Node(88)
l1.head.next = e2
e2.next = e3

print("Linked List: ")
l1.listing()

l1.AddAtBeginning(12)
l1.AddAtEnd(99)
l1.AddAtMiddle(5)

print("\nLinked List after Adding new elements: ")
l1.listing()