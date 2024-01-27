class Node:
    def __init__(self, val):
        self.info = val
        self.ptr = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_beg(self, val):
        node = Node(val)
        node.ptr = self.head
        self.head = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.info, end=" ")
            temp = temp.ptr

    def delete_kth_node(self, k):
        if not self.head or k <= 0:
            return

        if k == 1:
            self.head = self.head.ptr
        else:
            self._delete_kth_node_recursive(self.head, k, 1)

    def _delete_kth_node_recursive(self, current, k, count):
        if not current or not current.ptr:
            return

        if count == k - 1:
            current.ptr = current.ptr.ptr
        else:
            self._delete_kth_node_recursive(current.ptr, k, count + 1)


if __name__ == "__main__":
    
    obj = LinkedList()
    obj.insertion_at_beg(11)
    obj.insertion_at_beg(22)
    obj.insertion_at_beg(33)
    obj.insertion_at_beg(44)
    obj.insertion_at_beg(55)
    obj.insertion_at_beg(66)
    obj.print_list()
    print()
    pos = 5
    obj.delete_kth_node(pos)
    obj.print_list()