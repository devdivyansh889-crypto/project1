from add_books import add
from issue_book import issue
from shows_book import show
from return_book import return_book
from utils import current_day

def library():
    global current_day

    while True:
        print("\n=====LIBRARY MANAGEMENT SYSTEM=====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Next Day")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add()

        elif choice == 2:
            show()

        elif choice == 3:
            issue()

        elif choice == 4:
            return_book()

        elif choice == 5:
            current_day += 1
            print(f"Day advanced to: {current_day}")

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

library()