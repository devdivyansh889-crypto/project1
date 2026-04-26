from utils import books

def show():
    print("\n LIBRARY BOOK LIST")

    if len(books) == 0:
        print("No books available.")
    else:
        for book, details in books.items():
            print(f"\nBook: {book}")
            print(f"Status: {details['status']}")
            if details["status"] == "issued":
                print(f"Issued To: {details['student']}")