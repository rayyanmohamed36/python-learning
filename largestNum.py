largest = 0
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
if num1 > largest:
    largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print('The largest number is: ', largest)