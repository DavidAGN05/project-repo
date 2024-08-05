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

 
 
# Take input from the user
select = int(input("Please select operation -\n" \
    "1. Add\n" \
    "2. Subtract\n" \
    "3. Multiply\n" \
    "4. Divide\n" \
    "5. Modulus\n"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=", addition(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtraction(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=", multiplication(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=", division(number_1, number_2))

elif select == 5:
    print(number_1, "%", number_2, "=", modulus(number_1, number_2))

else:
    print("Invalid input")
