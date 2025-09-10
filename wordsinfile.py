import csv

filename = 'text.csv'

word_count = {}

try:
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            for cell in row:
                words = cell.split()
                for word in words:
                    word = word.lower()
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

    print("Word frequencies:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print("no file")
