class Node:
    def __init__(self,val):
        self.info = val
        self.ptr = None

class linklist:
    def __init__(self):
        self.head = None

    def InsertionAtBeg(self,val):
        node = Node(val)
        node.ptr = self.head
        self.head = node

    def printList(self):
        temp = self.head                                    
        count = 0                                           
        while temp:                                         
            print(temp.info, end = " " )                       
            temp = temp.ptr                                 
            count += 1                                      
        print(count)                                          
    
    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next = temp.ptr
            temp.ptr = prev 
            prev = temp 
            temp = next
        self.head = prev

    def delete(self):
        self.head = None

    def detectLoop(self):
        val_1 = self.head
        val_2 = self.head
        while(val_1 and val_2 and val_2.ptr):
            val_1 = val_1.ptr
            val_2 = val_2.ptr.ptr
            if val_1 == val_2:
                return 1
        return 0


if __name__ == "__main__":
    obj = linklist()
    obj.InsertionAtBeg(11)
    obj.InsertionAtBeg(22)
    obj.InsertionAtBeg(33)
    obj.printList()
    print()
    obj.head.ptr.ptr.ptr = obj.head
    if(obj.detectLoop()):
        print("Loop Found")
    else:
        print("No Loop")
    print()
    
    