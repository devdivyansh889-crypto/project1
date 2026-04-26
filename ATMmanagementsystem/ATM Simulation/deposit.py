from utils import balance, transactions

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: {amount}")
        print("Amount deposited successfully")
    else:
        print("Invalid amount")