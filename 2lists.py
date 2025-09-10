list1 = list(map(int, input("Enter numbers for first list separated by space: ").split()))
list2 = list(map(int, input("Enter numbers for second list separated by space: ").split()))

common = list(set(list1) & set(list2))

print("Common elements:", common)
