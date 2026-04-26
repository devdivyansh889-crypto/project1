from utils import books

def add():
    book_name = input("\nEnter Book Name: ").upper()

    if book_name in books:
        print(" Book already exists!!!")
    else:
        books[book_name] = {
            "status": "available",
            "student": "",
            "issue_day": 0,
            "days": 0
        }
        print("Book added successfully!!!")