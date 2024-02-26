def deposit(user, amount):
    balance = float(user[3])
    balance += amount
    user[3] = balance
    print(f"Deposited {amount}. New Balance: {user[3]}")


def withdraw(user, amount):
    balance = float(user[3])
    if balance >= amount:
        balance -= amount
        user[3] = balance
        print(f"Withdrawn {amount}. New Balance: {user[3]}")
    else:
        print("Insufficient funds.")


def generate_statement(user):
    print(f"Bank Statement for {user[1]}: \nBalance: {user[3]}")
