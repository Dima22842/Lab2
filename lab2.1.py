import csv


with open('books-en.csv', mode='r') as books:
    reader = csv.DictReader(books, delimiter=";")
    count = 0
    for data in reader:
        name = data['Book-Title']
        if len(name) >= 30:
            count += 1
print(count)