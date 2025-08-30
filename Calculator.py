def calcAdd(num1, num2):
    amount = num1 + num2
    return amount

def calcSubtract(num1, num2):
    amount = num1 - num2
    return amount

def calcMultiply(num1, num2):
    amount = num1 * num2
    return amount

def calcDivide(num1, num2):
    amount = num1 / num2
    return amount

choice = int(input('If you want to add two numbers enter 1, if you want to subtract two numbers enter 2, if you want to multiply two numbers enter 3, if you want to divivde two numbers enter 4'))

if choice == 1:
  num1 = int(input('enter the first number'))
  num2 = int(input(print('enter the second number')))
  print(calcAdd(num1, num2))

elif choice == 2:
  num1 = int(input('enter the first number'))
  num2 = int(input('enter the second number'))
  print(calcSubtract(num1, num2))

elif choice == 3:
  num1 = int(input('enter the first number'))
  num2 = int(input('enter the second number'))
  print(calcMultiply(num1, num2))

elif choice == 4:
  num1 = int(input('enter the first number'))
  num2 = int(input('enter the second number'))
  print(calcDivide(num1, num2))