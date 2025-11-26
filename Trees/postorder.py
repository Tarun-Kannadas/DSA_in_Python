class Node:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.val = key

def postorder_traversal(root):
    if (root):
        postorder_traversal(root.leftchild)
        postorder_traversal(root.rightchild)
        print(root.val, end = " ")

root = Node(56)
root.leftchild = Node(26)
root.rightchild = Node(45)
root.leftchild.leftchild = Node(12)
root.leftchild.rightchild = Node(14)
root.rightchild.leftchild = Node(32)
root.rightchild.rightchild = Node(28)

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
    print(node.val, end=" ")

print("\nPostorder Traversal: ")
postorder_traversal(root)
