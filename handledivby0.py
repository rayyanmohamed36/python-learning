numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))

try:
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
