import csv


author=input("Enter the author name: ")

with open('books-en.csv', mode = 'r') as books:
    reader = csv.DictReader(books, delimiter = ";")
    for data in reader:
        name_books = data['Book-Title']
        author_books = data['Book-Author']
        price_books = float(data['Price'].replace(",", "."))
        if price_books <= 150 and author_books == author:
            print(f"{name_books} - {price_books}")

