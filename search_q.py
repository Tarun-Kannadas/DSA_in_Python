class Node:
    def __init__(self,data=None):
        self.data=data
        self.next = None


class SLL:
    def printval(self):
        printval = self.head
        print("Linked List: ")
        while printval is not None:
            print(printval.data, end=" ")
            printval = printval.next
    
    def __init__(self):
        self.head = None

    def search(self,x):
        count = 0

        current = self.head

        while current != None:
            if current.data == x:
                print(f"Element {x} found at position")
                count = count + 1
            current = current.next
        if count == 0:
            print(f"Element {x} not found in the list")

l1 = SLL()
l1.head = Node("564")
e2 = Node("132")
e3 = Node("77")

l1.head.next = e2
e2.next = e3
l1.printval()
val = "56"
print("\nElement to be searched:", val)
l1.search(val)
val = "132"
print("Element to be searched:", val)
l1.search(val)
val = "91"
print("Element to be searched:", val)
l1.search(val)