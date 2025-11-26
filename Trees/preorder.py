class Node:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.val = key

def preorder_traversal(root):
    if root:
        print(root.val, end = " ")
        preorder_traversal(root.leftchild)
        preorder_traversal(root.rightchild)

root = Node(62)
root.leftchild = Node(35)
root.rightchild = Node(50)
root.leftchild.leftchild = Node(28)
root.leftchild.rightchild = Node(30)
root.rightchild.leftchild = Node(32)
root.rightchild.rightchild = Node(45)

print("Before Traversing: ")

arr = [
    root,
    root.leftchild,
    root.rightchild,
    root.leftchild.leftchild,
    root.leftchild.rightchild,
    root.rightchild.leftchild,
    root.rightchild.rightchild,
]

for node in arr:
    print(node.val, end = " ")

print("\nAfter Preorder Traversing: ")
preorder_traversal(root)