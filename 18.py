# Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Cannot divide by zero" if b == 0 else a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")
        choice = int(input("Enter choice: "))
#exit
        if choice == 7:
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print(add(a, b))
        elif choice == 2:
            print(subtract(a, b))
        elif choice == 3:
            print(multiply(a, b))
        elif choice == 4:
            print(divide(a, b))
        elif choice == 5:
            print(modulus(a, b))
        elif choice == 6:
            print(power(a, b))
        else:
            print("Invalid choice")
#run the calculator
calculator()