
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    if root is None:
        return 0
    return root.height

def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)

def rightRotate(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def leftRotate(x):
    y = x.right
    t = y.left

    y.left = x
    x.right = t

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and data < root.left.data:
        return rightRotate(root)

    if b < -1 and data > root.right.data:
        return leftRotate(root)

    if b > 1 and data > root.left.data:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if b < -1 and data < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def minNode(root):
    while root.left:
        root = root.left
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = minNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    if root is None:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return rightRotate(root)

    if b > 1 and balance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if b < -1 and balance(root.right) <= 0:
        return leftRotate(root)

    if b < -1 and balance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

root = None

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Inorder  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        x = int(input("Enter value to delete: "))
        root = delete(root, x)
    elif ch == 3:
        x = int(input("Enter value to search: "))
        if search(root, x):
            print("Element found")
        else:
            print("Element not found")
    elif ch == 4:
        inorder(root)
        print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
