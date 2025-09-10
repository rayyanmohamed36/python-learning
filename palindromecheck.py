numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers == numbers[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
