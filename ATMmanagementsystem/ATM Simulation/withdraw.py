from utils import balance, transactions

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        print("Please collect your cash")
    else:
        print("Insufficient balance")