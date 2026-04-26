from utils import books
from utils import current_day

def calculate_fine(late_days):
    fine = 0
    week = 1

    while late_days > 0:
        days_in_week = min(7, late_days)
        fine += days_in_week * (10 * week)
        late_days -= days_in_week
        week += 1

    return fine


def return_book():
    book_name = input("\nEnter Book Name to Return: ").upper()

    if book_name in books and books[book_name]["status"] == "issued":
        issue_day = books[book_name]["issue_day"]
        allowed_days = books[book_name]["days"]

        used_days = current_day - issue_day

        if used_days <= allowed_days:
            print("Book returned on time. No fine.")
        else:
            late_days = used_days - allowed_days
            fine = calculate_fine(late_days)
            print(f"Late by {late_days} days")
            print(f"Fine = ₹{fine}")

        # Reset book
        books[book_name]["status"] = "available"
        books[book_name]["student"] = ""

        print("Book returned successfully!!!")

    else:
        print("Invalid book or not issued!!!")