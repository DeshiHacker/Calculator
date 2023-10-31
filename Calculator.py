first = float(input("please enter first number: "))

operator = input("enter operator ('+','-','*','/','%'): ")
second = float(input("enter second number please: "))

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Invlide operation!")


print("manis.programmer@gmail.com")