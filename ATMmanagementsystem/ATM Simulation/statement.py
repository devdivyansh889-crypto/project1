from utils import transactions

def show_statement():
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        print("Transaction History:")
        for t in transactions:
            print(t)