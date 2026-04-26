from utils import books
from utils import current_day

def issue():
    book_name = input("\nEnter Book Name to Issue: ").upper()

    if book_name in books and books[book_name]["status"] == "available":
        student = input("Enter Student Name: ")
        days = int(input("Enter number of days: "))

        books[book_name]["status"] = "issued"
        books[book_name]["student"] = student
        books[book_name]["issue_day"] = current_day
        books[book_name]["days"] = days

        print("\n Book issued successfully!!!")

        print("\n NOTICE:")
        print("Late fine charges:")
        print("1st week → ₹10/day")
        print("2nd week → ₹20/day")
        print("3rd week → ₹60/day and so on")

    else:
        print("Book not available!!!")