class Node:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.val = key

def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.leftchild)
        preorder_traversal(root.rightchild)

root = Node(45)
root.leftchild = Node(28)
root.rightchild = Node(56)
root.leftchild.leftchild = Node(14)
root.leftchild.rightchild = Node(32)
root.rightchild.leftchild = Node(52)
root.rightchild.rightchild = Node(62)

print("Preorder Traversal: ")
preorder_traversal(root)