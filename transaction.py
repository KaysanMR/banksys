from logger import log_transaction

def deposit(user, amount):
    balance = float(user[3])
    balance += amount
    user[3] = balance
    log_transaction(user, None, amount, "Deposit")
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
        log_transaction(user, None, amount, "Withdraw")
        print(f"Withdrawn {amount}. New Balance: {user[3]}")
    else:
        print("Insufficient funds.")


def generate_statement(user):
    print(f"Bank Statement for {user[1]}: \nBalance: {user[3]}")





def transfer_funds(from_user, to_user, amount, user_list):
    from_user_balance = float(from_user[3])

    if from_user not in user_list or to_user not in user_list:
        print("One or more accounts not found.")
        return False

    if from_user_balance < amount:
        print("Insufficient funds in the source account.")
        return False

    from_user[3] = str(from_user_balance - amount)
    to_user[3] = str(float(to_user[3]) + amount)

    log_transaction(from_user, to_user, amount, "Transfer")

    print(f"Transferred {amount} from {from_user[1]} to {to_user[1]}.")
    return True
