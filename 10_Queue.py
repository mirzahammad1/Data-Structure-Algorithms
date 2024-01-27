def push(lis,val):
    lis.append(val)

def pop(lis):
    if len(lis) == 0:
        print("underflow")
        
    return lis.pop()

def EnQueue(lis,val):
    push(lis,val)

def DeQueue(lis):
    temp = []
    for i in range(len(lis)):
        temp.append(pop(lis))
    temp.pop()
    for i in range(len(temp)):
        EnQueue(lis,temp.pop())
    

if __name__ == "__main__":
    top = [0]
    lis=[]
    lis1 = []
    print()
    push(lis,99)
    push(lis,11)
    push(lis,22)
    EnQueue(lis,33)
    print(lis)
    DeQueue(lis)
    print()
