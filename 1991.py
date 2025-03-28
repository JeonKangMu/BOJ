class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def find(node, data):
    if node.data == data:
        return node
    if node.left:
        found = find(node.left, data)
        if found:
            return found
    if node.right:
        found = find(node.right, data)
        if found:
            return found
    return None

def preorder(node):
    print(node.data, end="")
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.data, end="")
    if node.right:
        inorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data, end="")

n = int(input().strip())
root = Node(None)

for i in range(n):
    a,b,c = map(str, input().split())
    if root.data is None:
        root.data = a

    pNode = find(root, a)
    if b != '.':
        pNode.left = Node(b)
    if c != '.':
        pNode.right = Node(c)

preorder(root)
print()
inorder(root)
print()
postorder(root)