def evaluation(P):
    stack = []
    for i in range(len(P)):
        operation = P[i]
        if (operation != "+" and operation != "-" and operation != "/" and operation != "*" and operation != "^"):
            stack.append(operation)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if operation == "+":
                result = a + b
                stack.append(result)
            elif operation == "-":
                result = a - b
                stack.append(result)
            elif operation == "*":
                result = a * b
                stack.append(result)
            elif operation == "/":
                result = a / b
                stack.append(result)
            elif operation == "^":
                result = a ^ b
                stack.append(result)
    return stack.pop()

if __name__ == "__main__":
    print()
    INfix = "12+23*"
    print(INfix)
    print(evaluation(INfix))
    print()
    userIn = input("Expression: ")
    print(evaluation(userIn))