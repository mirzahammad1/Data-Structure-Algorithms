def stack(lis,name):
        for i in range (len(name)):
            lis.append(name[i])

def pop(lis):
    if len(lis) == 0:
        print("underflow")
        return
    return lis.pop()

def is_balanced(input_string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for i in input_string:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(i):
                return False
    
    return len(stack) == 0


if __name__ == "__main__":
    name = input("ENTER NAME : ")
    lis = []
    val = ""

    stack(lis,name)
    print(lis)
    for i in range (len(lis)):
        val += pop(lis) 
    print(val)

    user_input = input("Enter a string with brackets: ")
    if is_balanced(user_input):
        print("balanced!")
    else:
        print("not balanced.")