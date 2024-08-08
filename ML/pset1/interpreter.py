def addition(x , y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def modulus(x, y):
    return x % y

equation = str.strip(input("Expression: "))
operations = ['+', '-', '*', '/', '%'] # does not work w/ negative #'s

for operation in operations:
# use iteration to loop which operation is being used
    if operation in equation:
        numbers = equation.split(operation)
        match operation:
            case '+':
                print(addition(int(numbers[0]), int(numbers[1])))
            case '-':
                print(subtraction(int(numbers[0]), int(numbers[1])))
            case '*':
                print(multiplication(int(numbers[0]), int(numbers[1])))
            case '/':
                print(division(int(numbers[0]), int(numbers[1])))
            case '%':
                print(modulus(int(numbers[0]), int(numbers[1])))
# .split(operation)