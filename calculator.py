def minus(a, b):
    '''This is  a  minus calculator'''
    return a - b

def plus(a, b):
    return a + b

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
dictionary = {
    "-": minus,
    "+": plus,
    "*": multiply,
    "/": divide,
}

def calculator():
    '''This is  calculator'''
    end = False
    num1 = float(input("Enter the first number: "))
    while not end:

        for key in dictionary:
            print(key)
        operation = input("Enter the operation: ")
        num2 = float(input("Enter next number: "))
        function = dictionary[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        check = input(f"Would you like to continue with {answer} type 'y' or 'n' to a new calculator. type 'e' to end the programm: ")
        if check == "y":
             num1 = answer

        elif check == "n":
            end = True
            calculator()
        else:
            end = True

calculator()
