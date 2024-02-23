def deposit(user, amount):
    user[3] += amount
    print(f"Deposited {amount}. New Balance: {user[3]}")

def withdraw(user, amount):
    if user[3] >= amount:
        user[3] -= amount
        print(f"Withdrawn {amount}. New Balance: {user[3]}")
    else:
        print("Insufficient funds.")

def generate_statement(user):
    print(f"Bank Statement for {user[1]}: \nBalance: {user[3]}")
