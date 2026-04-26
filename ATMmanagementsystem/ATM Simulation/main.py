from deposit import deposit
from withdraw import withdraw
from balance import show_balance
from statement import show_statement

def atm():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_statement()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")

atm()
