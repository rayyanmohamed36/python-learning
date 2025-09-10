numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)