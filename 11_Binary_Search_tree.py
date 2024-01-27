class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.Root = None

    def Insert(self, value):
        if self.Root is None:
            self.Root = TreeNode(value)
        else:
            ptr = self.Root
            while ptr is not None:
                if value < ptr.data:
                    if ptr.left is None:
                        ptr.left = TreeNode(value)
                        break
                    else:
                        ptr = ptr.left
                elif value >= ptr.data:
                    if ptr.right is None:
                        ptr.right = TreeNode(value)
                        break
                    else:
                        ptr = ptr.right

    def DecOrder(self, node):
        if node is not None:
            self.DecOrder(node.right)
            print(node.data, end=" ")
            self.DecOrder(node.left)

    def HighestValue(self):
        if self.Root is None:
            print("Tree is Empty")
            return None
        else:
            ptr = self.Root
            while ptr.right is not None:
                ptr = ptr.right
            print(ptr.data)

    def LowestValue(self):
        if self.Root is None:
            print("Tree is Empty")
            return None
        else:
            ptr = self.Root
            while ptr.left is not None:
                ptr = ptr.left
            print(ptr.data)

    def deleteLowestValue(self):
        if self.Root is None:
            print("Tree is Empty")
            return None
        else:
            ptr = self.Root
            while ptr.left.left:
                ptr = ptr.left
            ptr.left = None

if __name__ == "__main__":
    obj = BST()
    obj.Insert(8)
    obj.Insert(3)
    obj.Insert(10)
    obj.Insert(1)
    obj.Insert(6)
    obj.Insert(14)
    obj.Insert(4)
    obj.Insert(7)
    obj.Insert(13)

    print("DecOrder Traversal:")
    obj.DecOrder(obj.Root)

    print("\nHighest Value:")
    obj.HighestValue()

    print("Lowest Value:")
    obj.LowestValue()

    obj.deleteLowestValue()

    print("\nDecOrder Traversal after deletion:")
    obj.DecOrder(obj.Root)
