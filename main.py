from art import calculator_art


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def calculator():
    print(calculator_art)
    total = 0
    num1 = float(input("Enter the first number: "))
    for symbol in operation:
        print(symbol)
    continue_calculate = True

    while continue_calculate:
        symbol = input("Pick an operation: ")
        if symbol not in operation:
            print("Invalid Input")
            exit()
        num2 = float(input("Enter the next number: "))
        number_calculation = operation[symbol]
        total = number_calculation(num1, num2)
        print(f"{num1} {symbol} {num2} = {total}")
        num1 = total

        user_response = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to exit: ")
        if user_response == 'n':
            continue_calculate = False


calculator()
