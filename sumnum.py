def sum_numbers(*args):
    return sum(args)
user_input = input("Enter numbers separated by space: ")


numbers = list(map(int, user_input.split()))
total = sum_numbers(*numbers)

print("Sum of numbers:", total)
