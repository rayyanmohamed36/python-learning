def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = input("Enter a string: ")
print(char_frequency(string))
