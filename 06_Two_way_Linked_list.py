class Node:
    def __init__(self,value):
        self.info = value
        self.prev = None
        self.next = None

class Two_way_Linked_List:
    def __init__(self):
        self.head = None

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.info , end = " ")
            temp = temp.next

    def insert_strt(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            

    def Search(self, value):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            count = 1
            while temp != None and temp.info != value:
                temp = temp.next
                count += 1
            
            if temp == None:
                print(f"Value {value} Not Found in List")
            else:
                temp = temp.prev
                while temp:
                    print(temp.info , end = " ")
                    temp = temp.prev

if __name__ == "__main__":
    obj = Two_way_Linked_List()
    obj.insert_strt("PF")
    obj.insert_strt("OOP")
    obj.insert_strt("DST")
    obj.insert_strt("DBMS")
    obj.insert_strt("OOAD")
    obj.insert_strt("AI")
    obj.insert_strt("DP")
    obj.PrintList()
    print()
    user_input = input("ENTER YOUR COURSE: ")
    obj.Search(user_input)    
