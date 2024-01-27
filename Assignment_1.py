def Q1__DecimalToBinary(num):
    if num == 0:
        return "0"
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2
    return binary_str

def Q1__BinaryComplement(binary_str):
    complemented_str = ""
    for bit in binary_str:
        if bit == "0":
            complemented_str += "1"
        else:
            complemented_str += "0"
    return complemented_str

def Q1__BinaryToDecimal(complemented_str):
    decimal_num = 0
    complemented_str = complemented_str[::-1]  
    for i in range(len(complemented_str)):
        if complemented_str[i] == '1':
            decimal_num += 2 ** i
    return decimal_num

import numpy as np

def Q2__find_missing_elements(arr, low, high):
    range_bool = [False] * (high - low + 1)

    for x in arr:
        if low <= x <= high:
            range_bool[x - low] = True

    missing_elements = []
    for i in range(len(range_bool)):
        if not range_bool[i]:
            missing_elements.append(low + i)

    return missing_elements

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def createLinkedList(values):
        if not values:
            return None

        head = ListNode(values[0])
        current = head

        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        return head
    
    def printLinkedList(head):
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def deleteDuplicates(head):
        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return head

if __name__ == "__main__":
    dec_val = int(input("Enter a number: "))
    binary_rep = Q1__DecimalToBinary(dec_val)
    print("Binary representation:", binary_rep)

    complemented_rep = Q1__BinaryComplement(binary_rep)
    print("Binary complement:", complemented_rep)

    comp_decimal_rep = Q1__BinaryToDecimal(complemented_rep)
    print("Complement Decimal representation:", comp_decimal_rep)

    print()
    arr = np.array([1, 3, 5, 9])
    low = arr[0]
    high = arr[-1]
    missing_elements = Q2__find_missing_elements(arr, low, high)
    print("Missing elements in the range:", missing_elements)

    values = [0, 1, 1, 2, 3, 3, 4, 4, 4, 7, 7, 7, 9]
    head = ListNode.createLinkedList(values)

    print("Original Linked List:")
    ListNode.printLinkedList(head)
    
    new_head = ListNode.deleteDuplicates(head)
    
    print("Linked List after removing duplicates:")
    ListNode.printLinkedList(new_head)  