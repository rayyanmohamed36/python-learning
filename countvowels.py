string = str(input("Enter a string: "))
vowels = "aeiou"
count = 0
for letter in string:
    if letter.lower() in vowels:
        count = count + 1
print("vowels =", count)