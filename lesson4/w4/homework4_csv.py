#task1
import csv


def save_books(books):
    with open('books.txt','w',encoding='utf-8') as file:
        for book in books:
            file.write(book.strip() + '\n')

books = [
 	"Harry Potter",
 	"The Hobbit",
 	"1984",
 	"The Little Prince"
 ]

save_books(books)

#task2
with open('product.csv','w') as file:
    file.write('''product,price
 Coffee,25
 Tea,18
 Chocolate,12''')

def read_products(filename):
    with open('product.csv','r') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")

read_products('product.csv')

#task3
import json

def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country,
    }

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, indent=4, ensure_ascii=False)


save_user("anna21", "anna@example.com", "Israel")

#task4
from pathlib import Path

def create_logs_folder():
    log = Path("log")
    log.mkdir(exist_ok=True) #msdir opening file and exist_ok - checking if is valid
    #if exist_ok not valid - python will return ExistError
    file_path = log / "app.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Application started successfully!")

create_logs_folder()

with open(Path("log") / "app.txt", "r", encoding="utf-8") as file:
    print(file.read())
