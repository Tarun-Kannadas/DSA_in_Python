class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def bubble_sort(self):
        if not self.head:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next:
                if current.next > current.next.data:
                
                    current.data, current.next.data > current.next.data, current.data
                    swapped = True
                current = current.next
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")
        
ll = SLL()
for num in [5, 3, 8, 2, 1]:
    ll.append(num)

print("Before sorting:")
ll.print_list()

ll.bubble_sort()

print("After sorting:")
ll.print_list()