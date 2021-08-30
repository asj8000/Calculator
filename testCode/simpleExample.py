def plus(x,y):
    return x + y
def minus(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y

num1 = float(input("Enter first number: "))
choice = input("Enter type u chosen ( + - * / ) : ")
num2 = float(input("Enter second number: "))

if choice in ('+', '-', '*', '/'):
    print("result is ")
    if choice == '+':
        print(num1, " + ", num2, " = ", plus(num1, num2))
    elif choice == '-':
        print(num1, " - ", num2, " = ", minus(num1, num2))
    elif choice == '*':
        print(num1, " * ", num2, " = ", multiplication(num1, num2))
    elif choice == '/':
        print(num1, " / ", num2, " = ", division(num1, num2))
else:
    print("invalid input")