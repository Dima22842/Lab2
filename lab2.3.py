import csv
import random

name_books = []
author_books = []
year_books = []

for j in range(20):
    random_number = random.randint(1, 9409)
    with open('books-en.csv', mode='r') as books:
        reader = csv.DictReader(books, delimiter=";")
        for i, data in enumerate(reader, start=0):    
            if i == random_number:    
                name_books.append(data['Book-Title'])
                author_books.append(data['Book-Author'])
                year_books.append(data['Year-Of-Publication'])
                
with open('file.txt', 'w', encoding='utf-8') as file:
    for i in range(len(name_books)):
        file.write(f"{i+1}. {author_books[i]}. {name_books[i]} - {year_books[i]}\n")
