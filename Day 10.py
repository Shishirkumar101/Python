def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def multiply(n1, n2):
    return n1*n2

operations = {"+": add, "-": subtract, "/":divide, "*":multiply }

next = 'y'

first_number = float(input("Enter First number: "))

while(next == 'y'):
    for i in operations:
        print(i)
    operater = input("Pick an operation: ")
    second_number = float(input("Enter Second number: "))
    if operater in operations.keys():
        result = operations[operater](first_number , second_number)
    else:
        result, operater = 0 , 'undefine'
    print(f"{first_number} {operater} {second_number} = {result}")
    next = input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ")
    first_number = result

