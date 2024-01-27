class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None

    def push(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def circle(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head.prev = temp

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end = " " )
            temp = temp.next

if __name__ == "__main__":
    obj = Stack()
    obj.push(11)
    obj.push(22)
    obj.push(33)
    obj.printlist()
    print()
    obj.circle()
    print()
    obj.printlist()

 
