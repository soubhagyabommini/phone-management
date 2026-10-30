
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    while True:
        print("\n****** SIMPLE CALCULATOR ******")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("Enter you option: ")

        if option == "5":
            print("EXIT!")
            break

        if option not in ["1", "2", "3", "4"]:
            print("Invalid option")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if option == "1":
            print("Result:", addition(a, b))
        elif option == "2":
            print("Result:", subtraction(a, b))
        elif option == "3":
            print("Result:", multiplication(a, b))
        elif option == "4":
            print("Result:", division(a, b))

calculator()
