"""calculator
    This is a simple calculator where you ask the users for two numbers
    and try to
    perform some mathematical operations like {
        1.Addition
        2.Subtraction
        3. Multiplication
        4. Division
        5. Modulo
        6. Exponentiation
        7. Floor Division
    }
"""


def takeTwoNumbers() -> (int, int):
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))
    return (a, b)


def addition() -> int:
    firstNumber, secondNumber = takeTwoNumbers()
    result = firstNumber + secondNumber
    print(f"The result of {firstNumber} + {secondNumber} = {result}")


def subtraction() -> int:
    firstNumber, secondNumber = takeTwoNumbers()
    result = firstNumber - secondNumber
    print(f"The result of {firstNumber} - {secondNumber} = {result}")


def calculator():
    print("Starting All Engines")
    print("Select a number from 1-7 to perform an operation")
    print("1. Addition")
    print("2. SUBRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. MODULO")
    print("6. EXPONENTIATION")
    print("7. FLOOR DIVISION")
    userChoice = int(input("What is your choice? "))
    if (userChoice == 1):
        addition()
    elif userChoice == 2:
        subtraction()
    else:
        print("No valid choice detected")


calculator()
