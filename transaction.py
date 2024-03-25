
def deposit(user, amount):
    balance = float(user[3])
    balance += amount
    user[3] = balance
    print(f"Deposited {amount}. New Balance: {user[3]}")


def withdraw(user, amount):
    # balance = float(user[3])
    account_type = user[0](-1)
    withdraw_limit = 500 if account_type == "C" else 100
    if amount > withdraw_limit:
        print(f"Exceeds withdrawal limit for {account_type} account.")
        return

    balance = float(user[3])
    if balance >= amount:
        balance -= amount
        user[3] = balance
        print(f"Withdrawn {amount}. New Balance: {user[3]}")
    else:
        print("Insufficient funds.")


def generate_statement(user):
    print(f"Bank Statement for {user[1]}: \nBalance: {user[3]}")
